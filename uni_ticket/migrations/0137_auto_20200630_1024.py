# Generated by Django 3.0.7 on 2020-06-30 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uni_ticket', '0136_auto_20200626_1119'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='organizationalstructurewsarchipro',
            name='protocollo_cod_titolario',
        ),
        migrations.RemoveField(
            model_name='organizationalstructurewsarchipro',
            name='protocollo_fascicolo_anno',
        ),
        migrations.RemoveField(
            model_name='organizationalstructurewsarchipro',
            name='protocollo_fascicolo_numero',
        ),
        migrations.RemoveField(
            model_name='organizationalstructurewsarchipro',
            name='protocollo_id_uo',
        ),
        migrations.AlterField(
            model_name='ticketcategorywsarchipro',
            name='protocollo_cod_titolario',
            field=models.CharField(choices=[('9002', 'Normativa e relativa attuazione'), ('9003', 'Statuto'), ('9004', 'Regolamenti'), ('9005', 'Stemma, gonfalone e sigillo'), ('9006', "Sistema informativo, sicurezza dell'informazione e sistema informatico"), ('9007', 'Protezione dei dati personali'), ('9008', 'Archivio'), ('9009', 'Trasparenza e relazioni con il pubblico'), ('9010', 'Strategie per il personale, organigramma e funzionigramma'), ('9011', 'Rapporti sindacali e contrattazione'), ('9012', 'Controllo di gestione e sistema qualità'), ('9013', 'Statistica e auditing'), ('9014', 'Elezioni e designazioni'), ('9015', 'Associazioni e attività culturali, sportive e ricreative'), ('9016', 'Editoria e attività informativo-promozionale'), ('9017', 'Onorificenze, cerimoniale e attività di rappresentanza'), ('9018', 'Politiche e interventi per le pari opportunità'), ('9019', 'Interventi di carattere politico, economico, sociale e umanitario'), ('9021', 'Rettore'), ('9022', 'Prorettore vicario e delegati'), ('9023', 'Direttore generale'), ('9024', 'Direttore'), ('9025', 'Presidente'), ('9026', 'Senato accademico'), ('9027', 'Consiglio di amministrazione'), ('9028', 'Consiglio'), ('9029', 'Giunta'), ('9030', 'Commissione didattica paritetica docenti-studenti'), ('9031', 'Nucleo di valutazione'), ('9032', 'Collegio dei revisori dei conti'), ('9033', 'Collegio di disciplina (per i docenti)'), ('9034', 'Senato degli studenti'), ('9035', 'Comitato unico di garanzia e per le pari opportunità'), ('9036', 'Comitato tecnico scientifico'), ('9037', 'Conferenza dei rettori delle università italiane - CRUI'), ('9038', 'Comitato regionale di coordinamento'), ('9039', 'Comitato per lo sport universitario'), ('9041', 'Ordinamento didattico'), ('9042', 'Corsi di studio'), ('9043', 'Corsi a ordinamento speciale'), ('9044', 'Corsi di specializzazione'), ('9045', 'Master'), ('9046', 'Corsi di dottorato'), ('9047', 'Corsi di perfezionamento e corsi di formazione permanente'), ('9048', 'Programmazione didattica, orario delle lezioni, gestione delle aule e degli spazi'), ('9049', 'Gestione di esami di profitto, di laurea e di prove di idoneità'), ('9050', 'Programmazione e sviluppo, comprese aree, macroaree e settori scientifico-disciplinari'), ('9051', 'Strategie e valutazione della didattica e della ricerca'), ('9052', 'Premi e borse di studio finalizzati e vincolati'), ('9053', 'Progetti e finanziamenti'), ('9054', 'Accordi per la didattica e la ricerca'), ('9055', 'Rapporti con enti e istituti di area socio-sanitaria'), ('9056', "Opere dell'ingegno, brevetti e imprenditoria della ricerca"), ('9057', "Piani di sviluppo dell'università"), ('9058', 'Cooperazione con paesi in via di sviluppo'), ('9059', 'Attività per conto terzi'), ('9061', 'Contenzioso'), ('9062', 'Atti di liberalità'), ('9063', 'Violazioni amministrative e reati'), ('9064', 'Responsabilità civile, penale e amministrativa del personale'), ('9065', 'Pareri e consulenze'), ('9067', 'Orientamento, informazione e tutorato'), ('9068', 'Selezioni, immatricolazioni e ammissioni'), ('9069', 'Trasferimenti e passaggi'), ('9070', 'Cursus studiorum e provvedimenti disciplinari'), ('9071', 'Diritto allo studio, assicurazioni, benefici economici, tasse e contributi'), ('9072', 'Tirocinio, formazione e attività di ricerca'), ('9073', 'Servizi di assistenza socio-sanitaria e a richiesta'), ('9074', 'Conclusione e cessazione della carriera di studio'), ('9075', 'Esami di stato e ordini professionali'), ('9076', 'Associazionismo, goliardia e manifestazioni organizzate da studenti o ex studenti'), ('9077', 'Benefici Legge 390/91 '), ('9078', 'Servizi abitativi e mensa per gli studenti'), ('9079', 'Attività culturali e ricreative'), ('9081', 'Poli'), ('9082', 'Scuole e strutture di raccordo'), ('9083', 'Dipartimenti'), ('9084', 'Strutture a ordinamento speciale'), ('9085', 'Scuole di specializzazione'), ('9086', 'Scuole di dottorato'), ('9087', 'Scuole interdipartimentali'), ('9088', 'Centri'), ('9089', 'Sistema bibliotecario'), ('9090', 'Musei, pinacoteche e collezioni'), ('9091', 'Consorzi ed enti a partecipazione universitaria'), ('9092', 'Fondazioni'), ('9093', 'Servizi di ristorazione, alloggi e foresterie'), ('9095', 'Concorsi e selezioni'), ('9096', 'Assunzioni e cessazioni'), ('9097', 'Comandi e distacchi'), ('9098', 'Mansioni e incarichi'), ('9099', 'Carriera e inquadramenti'), ('9100', 'Retribuzione e compensi'), ('9101', 'Adempimenti fiscali, contributivi e assicurativi'), ('9102', 'Pre-ruolo, trattamento di quiescenza, buonuscita'), ('9103', 'Dichiarazioni di infermità ed equo indennizzo'), ('9104', 'Servizi a domanda individuale'), ('9105', 'Assenze'), ('9106', 'Tutela della salute e sorveglianza sanitaria'), ('9107', 'Valutazione, giudizi di merito e provvedimenti disciplinari'), ('9108', 'Formazione e aggiornamento professionale'), ('9109', 'Deontologia professionale ed etica del lavoro'), ('9110', 'Personale non strutturato'), ('9112', 'Ricavi ed entrate'), ('9113', 'Costi e uscite'), ('9114', 'Bilancio'), ('9115', 'Tesoreria, cassa e istituti di credito'), ('9116', 'Imposte, tasse, ritenute previdenziali e assistenziali'), ('9118', 'Progettazione e costruzione di opere edilizie con relativi impianti'), ('9119', "Manutenzione ordinaria, straordinaria, ristrutturazione, restauro e destinazione d'uso"), ('9120', 'Sicurezza e messa a norma degli ambienti di lavoro'), ('9121', 'Telefonia e infrastruttura informatica'), ('9122', 'Programmazione Territoriale'), ('9124', 'Acquisizione e gestione di beni immobili e relativi servizi'), ('9125', 'Locazione di beni immobili, di beni mobili e relativi servizi'), ('9126', 'Alienazione di beni immobili e di beni mobili'), ('9127', 'Acquisizione e fornitura di beni mobili, di materiali e attrezzature non tecniche e di servizi'), ('9128', 'Manutenzione di beni mobili'), ('9129', 'Materiali, attrezzature, impiantistica e adempimenti tecnico-normativi'), ('9130', 'Partecipazioni e investimenti finanziari'), ('9131', 'Inventario, rendiconto patrimoniale, beni in comodato'), ('9132', 'Patrimonio culturale – Tutela e valorizzazione'), ('9133', 'Gestione dei rifiuti'), ('9134', 'Albo dei fornitori'), ('9135', 'Oggetti diversi')], max_length=12, verbose_name='Codice titolario'),
        ),
    ]
