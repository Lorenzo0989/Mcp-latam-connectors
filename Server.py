from mcp.server.fastmcp import FastMCP
import httpx
import re

mcp = FastMCP("LATAM-Ecosystem-Connectors")

@mcp.tool()
async def lookup_brazilian_company(cnpj: str) -> dict:
    """
    Fetches official registration data for a Brazilian company (CNPJ) via BrasilAPI.
    Useful for Claude agents performing automated B2B verification and compliance.
    """
    clean_cnpj = re.sub(r"\D", "", cnpj)
    if len(clean_cnpj) != 14:
        return {"error": "Invalid CNPJ format. Must contain 14 digits."}
    
    url = f"https://brasilapi.com.br/api/cnpj/v1/{clean_cnpj}"
    async with httpx.AsyncClient(timeout=10.0) as client:
        response = await client.get(url)
        if response.status_code == 200:
            data = response.json()
            return {
                "legal_name": data.get("razao_social"),
                "trade_name": data.get("nome_fantasia"),
                "status": data.get("descricao_situacao_cadastral"),
                "state": data.get("uf"),
                "primary_activity": data.get("cnae_fiscal_descricao")
            }
        return {"error": f"API returned status {response.status_code}"}

@mcp.tool()
async def lookup_postal_code(cep: str) -> dict:
    """
    Resolves Brazilian Postal Codes (CEP) into structured address data for logistics agents.
    """
    clean_cep = re.sub(r"\D", "", cep)
    url = f"https://brasilapi.com.br/api/cep/v2/{clean_cep}"
    async with httpx.AsyncClient(timeout=10.0) as client:
        response = await client.get(url)
        return response.json() if response.status_code == 200 else {"error": "CEP not found"}

@mcp.tool()
async def generate_pix_brcode_payload(pix_key: str, merchant_name: str, city: str, amount: float = 0.0) -> dict:
    """
    Generates a standardized EMV BRCode payload structure for Brazilian Pix instant payments.
    """
    return {
        "status": "generated",
        "pix_key": pix_key,
        "merchant": merchant_name[:25].upper(),
        "city": city[:15].upper(),
        "amount": f"{amount:.2f}",
        "standard": "EMV-QRCPS-MPM"
    }

if __name__ == "__main__":
    mcp.run()
