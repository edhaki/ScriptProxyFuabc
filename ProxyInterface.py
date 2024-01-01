import tkinter as tk
from tkinter import messagebox
import subprocess
from PIL import Image, ImageTk
import base64

# Criador Ederson Alves da Silva - Analista de Desenvolvimento - Fundação do Abc - Contrato São Mateus. 
# Programa visa alternar proxy da instituição com da Prodam para fim de funcionamento da internet via redundancia.

def set_proxy(pac_url):
    try:
        # Define as configurações de proxy usando o arquivo PAC
        powershell_script = f'''
            $PacUrl = "{pac_url}"
            Set-ItemProperty -Path 'HKCU:\\Software\\Microsoft\\Windows\\CurrentVersion\\Internet Settings' -Name ProxyEnable -Value 1
            Set-ItemProperty -Path 'HKCU:\\Software\\Microsoft\\Windows\\CurrentVersion\\Internet Settings' -Name AutoConfigURL -Value "$PacUrl"
            Write-Host "Proxy configurado com sucesso."
        '''

        # Executa o script PowerShell diretamente do Python
        subprocess.run(["powershell.exe", "-Command", powershell_script], check=True)

        # Mostra mensagem de sucesso
        messagebox.showinfo("Proxy Ativado", "Proxy adicionado com sucesso.")

    except subprocess.CalledProcessError as e:
        messagebox.showerror("Erro", f"Erro ao configurar o proxy: {e}")

def disable_proxy():
    try:
        # Define as configurações de desativação de proxy
        powershell_script = '''
            Set-ItemProperty -Path 'HKCU:\\Software\\Microsoft\\Windows\\CurrentVersion\\Internet Settings' -Name ProxyEnable -Value 0
            Set-ItemProperty -Path 'HKCU:\\Software\\Microsoft\\Windows\\CurrentVersion\\Internet Settings' -Name AutoConfigURL -Value ""
            Remove-ItemProperty -Path 'HKCU:\\Software\\Microsoft\\Windows\\CurrentVersion\\Internet Settings' -Name AutoConfigURL
            Set-ItemProperty -Path 'HKCU:\\Software\\Microsoft\\Windows\\CurrentVersion\\Internet Settings' -Name ProxyServer -Value ""
            Write-Host "Proxy desativado com sucesso."
        '''

        # Executa o script PowerShell diretamente do Python
        subprocess.run(["powershell.exe", "-Command", powershell_script], check=True)

        # Mostra mensagem de sucesso
        messagebox.showinfo("Proxy Desativado", "Proxy removido com sucesso.")

    except subprocess.CalledProcessError as e:
        messagebox.showerror("Erro", f"Erro ao desativar o proxy: {e}")

def option_1():
    set_proxy("http://pac.prodam/proxy/sms.pac")

def option_2():
    disable_proxy()

def main():
    try:
        # Configurações da janela principal
        root = tk.Tk()
        root.title("Script de Internet Fundação do ABC - TI")
        root.geometry("680x250")

        # Conteúdo base64 do ícone
        icon_base64 = '''
            AAABAAEAEBAAAAEAIABoBAAAFgAAACgAAAAQAAAAIAAAAAEAIAAAAAAAAAAAAMQOAADEDgAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAa
AOL/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAbAOL/GgDi/xIA4f8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAaAOL/GgDi/xoA4v8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAenTxSwAAAAAAAAAA
AAAAABoA4v8aAOL/GgDi/xoA4v8AAAAAX6c4/wAAAAAAAAAAAAAAAAAAAAAAAAAAgykX/447LPAA
AAAAgXrwQxoA4v8aAOL/GgDi/wAAAAAAAAAANpAA/wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIMp
F/+DKRf/gykX/wAAAAAAAAAAAAAAAAAAAAAAAAAANpAA/ziRCf8AAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAACDKRf/gykX/4MpF/+DKRf/nFJEWgAAAAAAAAAAAAAAADaQAP8AAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAACDKRf/gykX/4MpF/8AAAAAAAAAADaQAP82kAD/AAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAL+ffwiDKRf/gykX/wAAAAA2kAD/NpAA/wAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgCQR/4MpF/8AAAAANpAA
/zaQAP8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDKRf/
AAAAADaQAP82kAD/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAA2kAD/LosA/wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAA//8AAP/vAAD/xwAA/48AAP4XAADcbwAAx88AAMPfAADxnwAA/J8AAPyfAAD+nwAA/58AAP//
AAD//wAA//8AAA==
        '''

        # Decodifica o ícone base64
        icon_data = base64.b64decode(icon_base64)
        
        # Salva o ícone em um arquivo temporário
        icon_path = "C:\\Users\\eders\\AppData\\Local\\Temp\\temp_icon.ico"
        with open(icon_path, "wb") as f:
            f.write(icon_data)

        # Carrega o ícone usando o Pillow
        icon_image = Image.open(icon_path)
        
        # Converte a imagem para o formato adequado para o Tkinter
        icon_photo = ImageTk.PhotoImage(icon_image)

        # Define o ícone da janela
        root.iconphoto(True, icon_photo)

        # Configuração de cores
        root.configure(bg="#FFFFFF")  # Cor de fundo branca
        
        # Impede o widget Label de ajustar automaticamente o tamanho do contêiner pai
        alert_label = tk.Label(root, text="Opção 1 : Em caso de queda na conexão da Fundação do ABC. \n \n Opção 2 : Quando Internet da instituição voltar ao normal clique em Internet Fundação do ABC.", font=("Arial", 12), bg="#FFFFFF")
        alert_label.pack(pady=10)
        alert_label.pack_propagate(False)
        
        # Cria botões para as opções 1 e 2
        option_1_button = tk.Button(root, text="Ativar Internet Prodam", command=option_1, font=("Arial", 14), bg="#008000", fg="#FFFFFF")
        option_2_button = tk.Button(root, text="Ativar Internet Fundação ABC", command=option_2, font=("Arial", 14), bg="#0000FF", fg="#FFFFFF")

        # Posiciona os botões na janela
        option_1_button.pack(pady=20)
        option_2_button.pack(pady=20)

        # Rodapé
        footer_label = tk.Label(root, text="Desenvolvido por Ederson Alves da Silva - TI", font=("Arial", 10), bg="#FFFFFF")
        footer_label.pack(pady=10)

        # Inicia o loop principal da interface gráfica
        root.mainloop()
    except Exception as e:
        print(f"Erro: {e}")

if __name__ == "__main__":
    main()
