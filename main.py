import requests
from bs4 import BeautifulSoup

cookies = {
    'ASP.NET_SessionId': 'rz5a4k5tsdldxwqjx0jxoua2',
    'loggedInLobIDCookie': '1',
    'tw_co_rcOZLj': '%7B%22widget_opened%22%3Afalse%7D',
}

headers = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="97", "Chromium";v="97"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'Origin': 'https://bsd.sos.mo.gov',
    'Upgrade-Insecure-Requests': '1',
    'DNT': '1',
    'Content-Type': 'application/x-www-form-urlencoded',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-User': '?1',
    'Sec-Fetch-Dest': 'document',
    'Referer': 'https://bsd.sos.mo.gov/BusinessEntity/BESearch.aspx?SearchType=0',
    'Accept-Language': 'zh-TW,zh;q=0.9',
}

params = (
    ('SearchType', '0'),
)

data = {
  'ctl00_ctl00_RadStyleSheetManager_TSSM': ';Telerik.Web.UI, Version=2021.1.224.45, Culture=neutral, PublicKeyToken=121fae78165ba3d4:en-US:668347d1-93a2-4485-86a0-60eda4ba4fe2:ed2942d4:45085116;Telerik.Web.UI.Skins, Version=2021.1.224.45, Culture=neutral, PublicKeyToken=121fae78165ba3d4:en-US:573f9d36-3267-486b-8c31-15cd157e7db4:21513f52',
  'ctl00_ctl00_externalWebRadScriptManager_TSM': ';;System.Web.Extensions, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35:en-US:4ff39ab4-86bc-4f97-a397-bc04a8fc5f51:ea597d4b:b25378d2;Telerik.Web.UI, Version=2021.1.224.45, Culture=neutral, PublicKeyToken=121fae78165ba3d4:en-US:668347d1-93a2-4485-86a0-60eda4ba4fe2:16e4e7cd:33715776:f7645509:24ee1bba:e330518b:2003d0b8:c128760b:1e771326:88144a7a:c8618e41:1a73651d:333f8d94:ed16cbdc',
  '__LASTFOCUS': '',
  '__EVENTTARGET': 'ctl00$ctl00$ContentPlaceHolderMain$ContentPlaceHolderMainSingle$ppBESearch$bsPanel$stdbtnSearch$LinkStandardButton',
  '__EVENTARGUMENT': '',
  '__VIEWSTATE': '/wEPDwULLTE5NzE0MzM3MTgPFgIeCVBhZ2VMb2JJRAIBFgJmD2QWAmYPZBYCAgMPZBYCAgEPZBYUAgEPZBYCAgEPFgQeA3NyYwVBfi9XZWJJbWFnZS5hc2h4P1JlYWRJbWFnZUZyb21DYWNoZT1UcnVlJkxvYWRCYW5uZXJJbWFnZT1UcnVlJmlkPTIeA2FsdAUcQnVzaW5lc3MgUmVnaXN0cmF0aW9uIEJhbm5lcmQCAw9kFgJmDw8WAh4HVmlzaWJsZWhkZAIEDxQrAAIUKwACDxYGHhxFbmFibGVFbWJlZGRlZEJhc2VTdHlsZXNoZWV0Zx4SUmVzb2x2ZWRSZW5kZXJNb2RlCylyVGVsZXJpay5XZWIuVUkuUmVuZGVyTW9kZSwgVGVsZXJpay5XZWIuVUksIFZlcnNpb249MjAyMS4xLjIyNC40NSwgQ3VsdHVyZT1uZXV0cmFsLCBQdWJsaWNLZXlUb2tlbj0xMjFmYWU3ODE2NWJhM2Q0AR4VRW5hYmxlRW1iZWRkZWRTY3JpcHRzZ2QQFgZmAgECAgIDAgQCBRYGFCsAAg8WCB4EVGV4dAUiQnVzaW5lc3MgUmVnaXN0cmF0aW9uIEZlZXMgJiBGb3Jtcx4LTmF2aWdhdGVVcmwFMmh0dHBzOi8vd3d3LnNvcy5tby5nb3YvYnVzaW5lc3MvY29ycG9yYXRpb25zL2Zvcm1zHgdUb29sVGlwBQxGZWVzICYgRm9ybXMeBlRhcmdldAUHX3BhcmVudGRkFCsAAg8WCB8HBRlCdXNpbmVzcyBSZWdpc3RyYXRpb24gRkFRHwgFJGh0dHBzOi8vd3d3LnNvcy5tby5nb3YvYnVzaW5lc3MvZmFxcx8JBRpGcmVxdWVudGx5IEFza2VkIFF1ZXN0aW9ucx8KBQdfcGFyZW50ZGQUKwACDxYIHwcFH0J1c2luZXNzIFJlZ2lzdHJhdGlvbiBIb21lIFBhZ2UfCAUsaHR0cHM6Ly93d3cuc29zLm1vLmdvdi9idXNpbmVzcy9jb3Jwb3JhdGlvbnMfCQURQ29ycG9yYXRpb25zIEhvbWUfCgUHX3BhcmVudGRkFCsAAg8WCB8HBSNCdXNpbmVzcyBSZWdpc3RyYXRpb24gT25saW5lIEZpbGluZx8IBSVodHRwczovL3d3dy5zb3MubW8uZ292L2JzZC91c2VyZ3VpZGVzHwkFFENvcnBvcmF0aW9uIFNlcnZpY2VzHwoFB19wYXJlbnRkZBQrAAIPFggfBwUgQnVzaW5lc3MgUmVnaXN0cmF0aW9uIENvbnRhY3QgVXMfCAU0aHR0cHM6Ly93d3cuc29zLm1vLmdvdi9idXNpbmVzcy9jb3Jwb3JhdGlvbnMvY29udGFjdB8JBQpDb250YWN0IFVzHwoFB19wYXJlbnRkZBQrAAIPFggfBwUfU3dpdGNoIHRvIEJ1c2luZXNzIFJlZ2lzdHJhdGlvbh8IBRovTG9naW5XZWxjb21lLmFzcHg/bG9iSUQ9MR8JBQRMYXdzHwoFB19wYXJlbnRkZA8WBmZmZmZmZhYBBXNUZWxlcmlrLldlYi5VSS5SYWRNZW51SXRlbSwgVGVsZXJpay5XZWIuVUksIFZlcnNpb249MjAyMS4xLjIyNC40NSwgQ3VsdHVyZT1uZXV0cmFsLCBQdWJsaWNLZXlUb2tlbj0xMjFmYWU3ODE2NWJhM2Q0ZBYMZg8PFggfBwUiQnVzaW5lc3MgUmVnaXN0cmF0aW9uIEZlZXMgJiBGb3Jtcx8IBTJodHRwczovL3d3dy5zb3MubW8uZ292L2J1c2luZXNzL2NvcnBvcmF0aW9ucy9mb3Jtcx8JBQxGZWVzICYgRm9ybXMfCgUHX3BhcmVudGRkAgEPDxYIHwcFGUJ1c2luZXNzIFJlZ2lzdHJhdGlvbiBGQVEfCAUkaHR0cHM6Ly93d3cuc29zLm1vLmdvdi9idXNpbmVzcy9mYXFzHwkFGkZyZXF1ZW50bHkgQXNrZWQgUXVlc3Rpb25zHwoFB19wYXJlbnRkZAICDw8WCB8HBR9CdXNpbmVzcyBSZWdpc3RyYXRpb24gSG9tZSBQYWdlHwgFLGh0dHBzOi8vd3d3LnNvcy5tby5nb3YvYnVzaW5lc3MvY29ycG9yYXRpb25zHwkFEUNvcnBvcmF0aW9ucyBIb21lHwoFB19wYXJlbnRkZAIDDw8WCB8HBSNCdXNpbmVzcyBSZWdpc3RyYXRpb24gT25saW5lIEZpbGluZx8IBSVodHRwczovL3d3dy5zb3MubW8uZ292L2JzZC91c2VyZ3VpZGVzHwkFFENvcnBvcmF0aW9uIFNlcnZpY2VzHwoFB19wYXJlbnRkZAIEDw8WCB8HBSBCdXNpbmVzcyBSZWdpc3RyYXRpb24gQ29udGFjdCBVcx8IBTRodHRwczovL3d3dy5zb3MubW8uZ292L2J1c2luZXNzL2NvcnBvcmF0aW9ucy9jb250YWN0HwkFCkNvbnRhY3QgVXMfCgUHX3BhcmVudGRkAgUPDxYIHwcFH1N3aXRjaCB0byBCdXNpbmVzcyBSZWdpc3RyYXRpb24fCAUaL0xvZ2luV2VsY29tZS5hc3B4P2xvYklEPTEfCQUETGF3cx8KBQdfcGFyZW50ZGQCBg8WAh4FY2xhc3MFEXN1Yi1oZWFkZXItYnV0dG9uZAIHDxYGHgRocmVmBSovQnVzaW5lc3NFbnRpdHkvQkVTZWFyY2guYXNweD9TZWFyY2hUeXBlPTAfCwUsc3ViLWhlYWRlci1idXR0b24gc3ViLWhlYWRlci1idXR0b24tc2VsZWN0ZWQeCWlubmVyaHRtbAUGU0VBUkNIZAIJDxYEHwwFGi9Mb2dpbldlbGNvbWUuYXNweD9sb2JJRD0wHw0FClVDQyBGSUxJTkdkAgsPFgIeB29uY2xpY2sFKGphdmFzY3JpcHQ6T3BlbkhlbHBGaWxlKCk7IHJldHVybiBmYWxzZTtkAhIPDxYCHwcFHFNlYXJjaCBmb3IgYSBCdXNpbmVzcyBFbnRpdHlkZAITD2QWAgIBD2QWAmYPZBYCAgMPZBYGAgEPFgIfA2gWAgIBDw8WBB8HZR8IBTRodHRwOi8vd3d3LnNvcy5tby5nb3YvYnVzaW5lc3MvY29ycG9yYXRpb25zL2ZhcXMuYXNwZGQCAw9kFgICAQ8PFgoeClBhZ2VGaWVsZHMy7gwAAQAAAP////8BAAAAAAAAAAwCAAAAVkZpbGVPbmUuU3lzdGVtV29ya3MuV2ViRXh0ZXJuYWwsIFZlcnNpb249MC4wLjAuMCwgQ3VsdHVyZT1uZXV0cmFsLCBQdWJsaWNLZXlUb2tlbj1udWxsBAEAAACoAVN5c3RlbS5Db2xsZWN0aW9ucy5HZW5lcmljLkxpc3RgMVtbRmlsZU9uZS5TeXN0ZW1Xb3Jrcy5XZWJFeHRlcm5hbC5TZWFyY2hGaWVsZCwgRmlsZU9uZS5TeXN0ZW1Xb3Jrcy5XZWJFeHRlcm5hbCwgVmVyc2lvbj0wLjAuMC4wLCBDdWx0dXJlPW5ldXRyYWwsIFB1YmxpY0tleVRva2VuPW51bGxdXQMAAAAGX2l0ZW1zBV9zaXplCF92ZXJzaW9uBAAALUZpbGVPbmUuU3lzdGVtV29ya3MuV2ViRXh0ZXJuYWwuU2VhcmNoRmllbGRbXQIAAAAICAkDAAAAAQAAAAEAAAAHAwAAAAABAAAABAAAAAQrRmlsZU9uZS5TeXN0ZW1Xb3Jrcy5XZWJFeHRlcm5hbC5TZWFyY2hGaWVsZAIAAAAJBAAAAA0DDAUAAABzRmlsZU9uZUZyYW1ld29yay5EYXRhQWNjZXNzU2VydmljZS5EYXRhQ29udHJhY3RzLCBWZXJzaW9uPTAuMC4wLjAsIEN1bHR1cmU9bmV1dHJhbCwgUHVibGljS2V5VG9rZW49ZDAzMmQxZWRhNDBiYzUxNwUEAAAAK0ZpbGVPbmUuU3lzdGVtV29ya3MuV2ViRXh0ZXJuYWwuU2VhcmNoRmllbGQCAAAAIDxTZWFyY2hGaWVsZFR5cGU+a19fQmFja2luZ0ZpZWxkIzxGaWVsZENvbmZpZ3VyYXRpb24+a19fQmFja2luZ0ZpZWxkBAQvRmlsZU9uZS5TeXN0ZW1Xb3Jrcy5XZWJFeHRlcm5hbC5TZWFyY2hGaWVsZFR5cGUCAAAASEZpbGVPbmVGcmFtZXdvcmsuRGF0YUFjY2Vzc1NlcnZpY2UuRGF0YUNvbnRyYWN0cy5jZk9ubGluZVZpc2libGVSZXFGaWVsZAUAAAACAAAABfr///8vRmlsZU9uZS5TeXN0ZW1Xb3Jrcy5XZWJFeHRlcm5hbC5TZWFyY2hGaWVsZFR5cGUBAAAAB3ZhbHVlX18ACAIAAAABAAAACQcAAAAFBwAAAEhGaWxlT25lRnJhbWV3b3JrLkRhdGFBY2Nlc3NTZXJ2aWNlLkRhdGFDb250cmFjdHMuY2ZPbmxpbmVWaXNpYmxlUmVxRmllbGQTAAAAGF9PbmxpbmVWaXNpYmxlUmVxRmllbGRJRBNfT25saW5lRmlsaW5nUGFnZUlEEl9PbmxpbmVQYWdlRmllbGRJRAtfRmllbGRMYWJlbBFfRmllbGREZXNjcmlwdGlvbhFfRmllbGRJbnN0cnVjdGlvbgpfSXNWaXNpYmxlC19Jc1JlcXVpcmVkDV9Jc01vZGlmaWFibGURX0RlZmF1bHRCb29sVmFsdWUQX0RlZmF1bHRJbnRWYWx1ZRFfRGVmYXVsdFRleHRWYWx1ZQ9fRG9jdW1lbnRUeXBlSWQLX0lzRGlzYWJsZWQUX0lzQXBwZW5kVG9GaWxlZENvcHkSX1JlY29yZGluZ1VzZXJOYW1lDl9SZWNvcmRpbmdUaW1lC19Sb3dWZXJzaW9uLURiT2JqZWN0QmFzZVRhYmxlKzxSb3dWZXJzaW9uPmtfX0JhY2tpbmdGaWVsZAAAAAEBAQAAAAADAQMAAAEAAAAICAgBAQEBblN5c3RlbS5OdWxsYWJsZWAxW1tTeXN0ZW0uSW50MzIsIG1zY29ybGliLCBWZXJzaW9uPTQuMC4wLjAsIEN1bHR1cmU9bmV1dHJhbCwgUHVibGljS2V5VG9rZW49Yjc3YTVjNTYxOTM0ZTA4OV1dblN5c3RlbS5OdWxsYWJsZWAxW1tTeXN0ZW0uSW50MzIsIG1zY29ybGliLCBWZXJzaW9uPTQuMC4wLjAsIEN1bHR1cmU9bmV1dHJhbCwgUHVibGljS2V5VG9rZW49Yjc3YTVjNTYxOTM0ZTA4OV1dAQENCAgFAAAAAAAAAAAAAAAAAAAABggAAAAGU0VBUkNICgoBAAAACgoKAAAGCQAAAAAfnUm0SubZiAAAAAAAAAAACx4cU2VhcmNoQ29udHJvbFZhbGlkYXRpb25Hcm91cAUKdmdCRVNlYXJjaB4UU2VhcmNoVHlwZUZvckNvbnRyb2xmHg9DYW5TZWFyY2hFbnRpdHloHiFJc0lEb05vdFdhbnRUb1NlYXJjaEJ1dHRvblZpc2libGVoZBYKAgIPZBYCAgEPZBYEAgEPDxYEHwcFngFFeGFjdCBNYXRjaCBzZWFyY2hlcyBzaG91bGQgaW5jbHVkZSBjb3Jwb3JhdGUgZGVzaWduYXRpb25zIChpbmMuLCBsbGMsIGV0Yy4pIGFuZCBwdW5jdHVhdGlvbi4gPGJyIC8+IFdlIHJlY29tbWVuZCB5b3UgZG8gbm90IGluY2x1ZGUgdGhlc2UgZm9yIG90aGVyIHNlYXJjaGVzLh8DZ2RkAgsPEGQQFQQNQnVzaW5lc3MgTmFtZRBSZWdpc3RlcmVkIEFnZW50EU5hbWUgQXZhaWxhYmlsaXR5C0NoYXJ0ZXIgTm8uFQQBMAExATIBMxQrAwRnZ2dnFgFmZAIED2QWCAIBDxYCHwNnFgoCAQ8PFgIfBwUcU2VhcmNoIGZvciBhIEJ1c2luZXNzIEVudGl0eWRkAgMPDxYEHg9WYWxpZGF0aW9uR3JvdXAFCnZnQkVTZWFyY2geDEVycm9yTWVzc2FnZQUcLSBCdXNpbmVzcyBOYW1lIGlzIHJlcXVpcmVkLmQWAmYPFgIeBXRpdGxlBRlCdXNpbmVzcyBOYW1lIGlzIHJlcXVpcmVkZAIFDw8WAh8HBQ1CdXNpbmVzcyBOYW1lZGQCCw8QZA8WBGYCAQICAgMWBBAFDVN0YXJ0aW5nIFdpdGgFATBnEAUJQWxsIFdvcmRzBQExZxAFCEFueSBXb3JkBQEyZxAFC0V4YWN0IE1hdGNoBQEzZ2RkAg0PEA8WAh8HBRhPbmx5IEFjdGl2ZSBDb3Jwb3JhdGlvbnNkZGRkAgMPZBYEAgMPDxYCHxQFCnZnQkVTZWFyY2hkZAIHDw8WAh8HZWRkAgUPZBYEAgUPDxYCHwdlZGQCBw8PFgIfFAUKdmdCRVNlYXJjaGRkAgcPZBYMAgMPEGRkFgFmZAIFDw8WAh8UBQp2Z0JFU2VhcmNoZGQCCw8PFgIfB2VkZAINDw8WAh8HZWRkAhEPDxYCHwdlZGQCFQ8QZA8WBGYCAQICAgMWBBAFDVN0YXJ0aW5nIFdpdGgFATBnEAUJQWxsIFdvcmRzBQExZxAFCEFueSBXb3JkBQEyZxAFC0V4YWN0IE1hdGNoBQEzZxYBZmQCBg8PFgIfA2hkFgJmD2QWAmYPZBYEAgMPFgQfDQUBLR8LBR5zd1RlbXBsYXRlQnV0dG9uRGl2VGV4dFRvcExlZnRkAgUPFgQfDQUBLR8LBSFzd1RlbXBsYXRlQnV0dG9uRGl2VGV4dEJvdHRvbUxlZnRkAgoPZBYCZg8PFg4fCQUGU2VhcmNoHhBDYXVzZXNWYWxpZGF0aW9uZx4PQ29tbWFuZEFyZ3VtZW50ZB4LQ29tbWFuZE5hbWVkHgtQb3N0QmFja1VybGQfFAUKdmdCRVNlYXJjaB4IVGFiSW5kZXgBAABkFgJmD2QWBAIDDxYEHw0FBlNFQVJDSB8LBSFzd1RlbXBsYXRlQnV0dG9uSWNvbkRpdlRleHRDZW50ZXJkAgUPFgIfDWVkAgwPZBYEAgMPPCsADgIAFCsAAmQXAQUIUGFnZVNpemUCFAEWAhYLDwIMFCsADDwrAAUBBAUMU2VsZWN0Q29sdW1uPCsABQEEBRRHcmlkQnVzaW5lc3NFbnRpdHlJRDwrAAUBBAUKU1dFbnRpdHlJRDwrAAUBBAUPQkVOYW1lRGF0YUJvdW5kFCsABRYCHgpIZWFkZXJUZXh0BQ1CdXNpbmVzcyBOYW1lZGRkBQpHcmlkQkVOYW1lPCsABQEEBQlCRUFkZHJlc3MUKwAFFgIfHAULQ2hhcnRlciBOby5kZGQFGkdyaWRCdXNpbmVzc0VudGl0eUlETnVtYmVyFCsABRYCHxwFBFR5cGVkZGQFCkdyaWRCRVR5cGUUKwAFFgIfHAUGU3RhdHVzZGRkBQxHcmlkQkVTdGF0dXM8KwAFAQQFDUdyaWRJc1ByaW1hcnkUKwAFFgIfHAUHQ3JlYXRlZGRkZAUOR3JpZERhdGVGb3JtZWQUKwAFFgIfHAUVUmVnaXN0ZXJlZCBBZ2VudCBOYW1lZGRkBQxHcmlkUmVnQWdlbnRkZRQrAAALKXlUZWxlcmlrLldlYi5VSS5HcmlkQ2hpbGRMb2FkTW9kZSwgVGVsZXJpay5XZWIuVUksIFZlcnNpb249MjAyMS4xLjIyNC40NSwgQ3VsdHVyZT1uZXV0cmFsLCBQdWJsaWNLZXlUb2tlbj0xMjFmYWU3ODE2NWJhM2Q0ATwrAAcACyl0VGVsZXJpay5XZWIuVUkuR3JpZEVkaXRNb2RlLCBUZWxlcmlrLldlYi5VSSwgVmVyc2lvbj0yMDIxLjEuMjI0LjQ1LCBDdWx0dXJlPW5ldXRyYWwsIFB1YmxpY0tleVRva2VuPTEyMWZhZTc4MTY1YmEzZDQBZGRkZGZkAgUPPCsADgIAFCsAAmQXAQUIUGFnZVNpemUCFAEWAhYLDwIHFCsABzwrAAUBBAUOR3JpZFJlZ0FnZW50SUQ8KwAFAQQFGEdyaWRSZWdBZ2VudEVudGl0eVJlY29yZDwrAAUBBAUQR3JpZFJlZ0FnZW50TmFtZTwrAAUBBAUSR3JpZFJlZ0FnZW50T2ZmaWNlPCsABQEEBRZHcmlkUmVnQWdlbnRSZXByZXNlbnRzPCsABQEEBQ5HcmlkQkVJRE51bWJlcjwrAAUBBAUMR3JpZEJFU3RhdHVzZGUUKwAACysFATwrAAcACysGAWRkZGRmZAIFDxYCHwNoZAIVDw8WBB8GZx8EZ2RkGAEFHl9fQ29udHJvbHNSZXF1aXJlUG9zdEJhY2tLZXlfXxYCBShjdGwwMCRjdGwwMCRBZGRpdGlvbmFsUXVpY2tMaW5rc0xlZnRNZW51BV9jdGwwMCRjdGwwMCRDb250ZW50UGxhY2VIb2xkZXJNYWluJENvbnRlbnRQbGFjZUhvbGRlck1haW5TaW5nbGUkcHBCRVNlYXJjaCRic1BhbmVsJGNiQWN0aXZlT25seVnRD1IMhjUpcWRwphxUD7lW9QCIIt3/vqTAyH3/AcuB',
  '__VIEWSTATEGENERATOR': 'EDA4642F',
  'ctl00_ctl00_AdditionalQuickLinksLeftMenu_ClientState': '',
  'ctl00$ctl00$ContentPlaceHolderMain$ContentPlaceHolderMainSingle$ppBESearch$bsPanel$ddlBESearchType': '0',
  'ctl00$ctl00$ContentPlaceHolderMain$ContentPlaceHolderMainSingle$ppBESearch$bsPanel$hfSelectedBESearchType': '0',
  'ctl00$ctl00$ContentPlaceHolderMain$ContentPlaceHolderMainSingle$ppBESearch$bsPanel$tbBusinessName': 'A',
  'ctl00$ctl00$ContentPlaceHolderMain$ContentPlaceHolderMainSingle$ppBESearch$bsPanel$ddlNameSearchMethod': '0',
  'ctl00$ctl00$ContentPlaceHolderMain$ContentPlaceHolderMainSingle$ppBESearch$bsPanel$cbActiveOnly': 'on',
  'ctl00$ctl00$ContentPlaceHolderMain$ContentPlaceHolderMainSingle$ppBESearch$hdnBusinessEntitySearchControlID': 'ctl00_ctl00_ContentPlaceHolderMain_ContentPlaceHolderMainSingle_ppBESearch_bsPanel_stdbtnSearch_LinkStandardButton'
}

response = requests.post('https://bsd.sos.mo.gov/BusinessEntity/BESearch.aspx', headers=headers, params=params, data=data)

f = open("index.html", "w")
f.truncate(0)
f.write(response.text)
f.close()

# list_header = []
# path = 'index.html'
# soup = BeautifulSoup(open(path),'html.parser')
# header = soup.find_all("table", id="ctl00_ctl00_ContentPlaceHolderMain_ContentPlaceHolderMainSingle_ppBESearch_bsPanel_SearchResultGrid_ctl00")[0].find("thead")
  
# for items in header:
#     try:
#         list_header.append(items.get_text())
#     except:
#         continue

# print(list_header)

# HTML_data = soup.find_all("table", id="ctl00_ctl00_ContentPlaceHolderMain_ContentPlaceHolderMainSingle_ppBESearch_bsPanel_SearchResultGrid_ctl00")[0].find("tr")

# data_from_form = []
# for element in HTML_data:
#     sub_data = []
#     for sub_element in element:
#         try:
#             sub_data.append(sub_element.get_text())
#         except:
#             continue
#     data_from_form.append(sub_data)
# print(data_from_form)