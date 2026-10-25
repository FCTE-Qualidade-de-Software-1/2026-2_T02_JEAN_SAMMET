import json
import urllib.error
import urllib.parse
import urllib.request

URL_BASE = "https://api.github.com"
ITENS_POR_PAGINA = 100
TEMPO_LIMITE_SEGUNDOS = 30


class ErroApi(Exception):
    def __init__(self, status: int, mensagem: str):
        super().__init__(f"HTTP {status}: {mensagem}")
        self.status = status
        self.mensagem = mensagem


class ClienteGithub:
    def __init__(self, token: str, url_base: str = URL_BASE):
        self.token = token
        self.url_base = url_base

    def requisitar(self, metodo: str, caminho: str, parametros: dict | None = None, corpo: dict | None = None):
        endereco = self.url_base + caminho
        if parametros:
            endereco += "?" + urllib.parse.urlencode(parametros)
        dados = json.dumps(corpo).encode("utf-8") if corpo is not None else None
        requisicao = urllib.request.Request(endereco, data=dados, method=metodo)
        requisicao.add_header("Accept", "application/vnd.github+json")
        requisicao.add_header("X-GitHub-Api-Version", "2022-11-28")
        requisicao.add_header("User-Agent", "metricas-psm-cid")
        if self.token:
            requisicao.add_header("Authorization", f"Bearer {self.token}")
        if dados is not None:
            requisicao.add_header("Content-Type", "application/json")
        try:
            with urllib.request.urlopen(requisicao, timeout=TEMPO_LIMITE_SEGUNDOS) as resposta:
                conteudo = resposta.read()
        except urllib.error.HTTPError as erro:
            raise ErroApi(erro.code, erro.read().decode("utf-8", "replace")) from erro
        if not conteudo:
            return None
        return json.loads(conteudo)

    def listar(self, caminho: str, parametros: dict | None = None) -> list:
        resultado: list = []
        pagina = 1
        while True:
            filtros = dict(parametros or {})
            filtros["per_page"] = ITENS_POR_PAGINA
            filtros["page"] = pagina
            itens = self.requisitar("GET", caminho, filtros)
            resultado.extend(itens)
            if len(itens) < ITENS_POR_PAGINA:
                return resultado
            pagina += 1

    def enviar(self, metodo: str, caminho: str, corpo: dict | None = None):
        return self.requisitar(metodo, caminho, None, corpo)
