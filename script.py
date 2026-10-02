import os
import rawpy
import argparse # NOVITA: Modulo per gestire gli argomenti da terminale
from PIL import Image

def converti_cr2_in_jpg(cartella_origine):
    # Controlliamo che la cartella inserita esista davvero
    if not os.path.exists(cartella_origine):
        print(f"Errore: La cartella '{cartella_origine}' non esiste.")
        return

    # Creiamo la cartella di destinazione
    cartella_destinazione = os.path.join(cartella_origine, "converted_in_jpg")
    
    # Questo comando crea la cartella sul tuo computer. 
    # exist_ok=True significa: "Se la cartella c'e gia, non dare errore e vai avanti".
    os.makedirs(cartella_destinazione, exist_ok=True)
    
    print(f"I file convertiti verranno salvati in: {cartella_destinazione}")

    # Troviamo tutti i file nella cartella che finiscono per .cr2
    file_nella_cartella = os.listdir(cartella_origine)
    file_cr2 = [f for f in file_nella_cartella if f.lower().endswith('.cr2')]

    if len(file_cr2) == 0:
        print("Nessun file .cr2 trovato in questa cartella.")
        return

    print(f"Trovati {len(file_cr2)} file CR2. Inizio la conversione...")

    # Cicliamo attraverso ogni file CR2 trovato
    for nome_file in file_cr2:
        percorso_completo_cr2 = os.path.join(cartella_origine, nome_file)
        
        # Creiamo il nome del nuovo file JPG (es. 'foto' diventa 'foto.jpg')
        nome_senza_estensione = os.path.splitext(nome_file)[0]
        
        # Aggiorniamo il percorso di salvataggio
        percorso_completo_jpg = os.path.join(cartella_destinazione, f"{nome_senza_estensione}.jpg")
        
        print(f"Sto convertendo: {nome_file} ...")
        
        try:
            # rawpy.imread apre il file RAW vero e proprio
            with rawpy.imread(percorso_completo_cr2) as raw:
                # Elaboriamo il RAW con i colori originali della fotocamera
                dati_rgb = raw.postprocess(use_camera_wb=True)
            
            # Trasformiamo i dati grezzi in un'immagine che Python puo gestire
            immagine = Image.fromarray(dati_rgb)
            
            # Salviamo l'immagine in JPG nella NUOVA cartella
            immagine.save(percorso_completo_jpg, 'JPEG', quality=95)
            
            print(f"  -> Completato: salvato in 'converted_in_jpg'")
            
        except Exception as e:
            print(f"Si e verificato un errore con {nome_file}: {e}")

    print("\nConversione di tutti i file terminata con successo!")

# --- NOVITA: Gestione degli argomenti da terminale ---
# Questo blocco viene eseguito solo quando lanci lo script dal prompt dei comandi
if __name__ == "__main__":
    # 1. Creiamo l'oggetto che analizza i comandi
    parser = argparse.ArgumentParser(description="Converte tutte le foto CR2 di una cartella in JPG.")
    
    # 2. Diciamo a Python che ci aspettiamo un testo (il percorso)
    parser.add_argument("directory", help="Il percorso completo della cartella con le foto CR2")
    
    # 3. Leggiamo cosa ha scritto l'utente nel terminale
    args = parser.parse_args()
    
    # 4. Avviamo la nostra funzione passandole il percorso letto
    converti_cr2_in_jpg(args.directory)