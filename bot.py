from telegram.ext import Updater
from telegram import Update
from telegram.ext import CallbackContext
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler
from telegram.ext.filters import Filters

updater = Updater("6208908073:AAEuFcs9HUyJkeGFqWZtmZKKDHww7HI7bF0",
				use_context=True)


def start(update: Update, context: CallbackContext):
	update.message.reply_text(
		"Hallo Selamat Datang di Pusat Bantuan PPDB silahkan ketik\
		/help untuk melihat kata kunci yang dapat digunakan.")

def help(update: Update, context: CallbackContext):
	update.message.reply_text("""Available Commands :-
	/Seputar_ppdb - To get the youtube URL
	/Jalur_zonasi - To get the LinkedIn profile URL
	/Jalur Afirmasi - To get gmail URL
	/geeks - To get the GeeksforGeeks URL""")


def peryaratan_ppdb(update: Update, context: CallbackContext):
	update.message.reply_text("""
    UMUM
    - Ijazah/Surat Keterangan Lulus/Kartu peserta Ujian Sekolah
    - Akta Kelahiran/Surat Keterangan Lahir
    - Kartu Keluarga (minimal satu tahun), KTP
    - Buku Rapor (semester 1 s.d. 5)
    - Surat Tanggung Jawab Mutlak Orang Tua

    KHUSUS
    - Kartu Program Penanganan Kemiskinan/Terdaftar pada DTKS Dinsos (bagi jalur - afirmasi/KETM)
    - Surat Keterangan Domisili dari RT/RW (bagi afirmasi korban bencana alam/sosial)
    - Surat Tugas Orangtua (bagi jalur perpindahan tugas orangtua/wali, maks. 3 tahun/anak guru)
    - Surat keputusan satgas covid bagi afirmasi kondisi tertentu penanganan Covid-19
    - Piagam dan Dokumentasi Prestasi (untuk jalur prestasi kejuaraan) maks. 5 tahun, min. 6 bulan
	""")


def youtube_url(update: Update, context: CallbackContext):
	update.message.reply_text("Youtube Link =>\
	https://www.youtube.com/")


def linkedIn_url(update: Update, context: CallbackContext):
	update.message.reply_text(
		"LinkedIn URL => \
		https://www.linkedin.com/in/dwaipayan-bandyopadhyay-007a/")


def geeks_url(update: Update, context: CallbackContext):
	update.message.reply_text(
		"GeeksforGeeks URL => https://www.geeksforgeeks.org/")


def unknown(update: Update, context: CallbackContext):
	update.message.reply_text(
		"Sorry '%s' is not a valid command" % update.message.text)


def unknown_text(update: Update, context: CallbackContext):
	update.message.reply_text(
		"Sorry I can't recognize you , you said '%s'" % update.message.text)


updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('youtube', youtube_url))
updater.dispatcher.add_handler(CommandHandler('help', help))
updater.dispatcher.add_handler(CommandHandler('linkedin', linkedIn_url))
updater.dispatcher.add_handler(CommandHandler('persyaratan_ppdb', peryaratan_ppdb))
updater.dispatcher.add_handler(CommandHandler('geeks', geeks_url))
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown))
updater.dispatcher.add_handler(MessageHandler(
	Filters.command, unknown)) # Filters out unknown commands

# Filters out unknown messages.
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown_text))

updater.start_polling()
