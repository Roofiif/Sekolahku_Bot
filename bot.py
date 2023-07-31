from telegram.ext import Updater
from telegram import Update, ParseMode
from telegram.ext import CallbackContext
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler
from telegram.ext.filters import Filters

updater = Updater("6208908073:AAEuFcs9HUyJkeGFqWZtmZKKDHww7HI7bF0",
				use_context=True)


def start(update: Update, context: CallbackContext):
	update.message.reply_text(
		"Hallo Selamat Datang di Pusat Bantuan PPDB silahkan ketik\
		'<b>Bantuan</b>' untuk melihat kata kunci yang dapat digunakan.", parse_mode=ParseMode.HTML)

def bantuan(update: Update, context: CallbackContext):
	update.message.reply_text("""
	Kata Kunci Tersedia :
	<b>Seputar_ppdb</b> - Berisi informasi umum mengenai PPDB
	<b>Persyaratan_ppdb</b> - Berisi persyaratan PPDB
	""", parse_mode=ParseMode.HTML)


def seputar_ppdb(update: Update, context: CallbackContext):
	update.message.reply_text("""
	Seputar PPDB
	Kata Kunci Tersedia :
	<b>Jalur_ppdb</b> - Berisi informasi jalur yang tersedia
	<b>Nilai_prestasi</b> - Berisi informasi Nilai tambahan
	<b>Daftar_ulang</b> - Berisi informasi Daftar ulang
	""", parse_mode=ParseMode.HTML)


def jalur_ppdb(update: Update, context: CallbackContext):
	update.message.reply_text("""
	Jalur PPDB
	Kata Kunci Tersedia :
	<b>Jalur_zonasi</b> - Berisi informasi jalur Zonasi
	<b>Jalur_afirmasi</b> - Berisi informasi jalur aformasi
	<b>Jalur_prestasi</b> - Berisi informasi jalur Prestasi
	<b>Jalur_pto</b> - Berisi informasi jalur pto
	""", parse_mode=ParseMode.HTML)

def daftar_ulang(update: Update, context: CallbackContext):
	update.message.reply_text("""
	""", parse_mode=ParseMode.HTML)

def nilai_prestasi(update: Update, context: CallbackContext):
	update.message.reply_text("""
	""", parse_mode=ParseMode.HTML)

def jalur_zonasi(update: Update, context: CallbackContext):
	update.message.reply_text("""
	""", parse_mode=ParseMode.HTML)

def jalur_afirmasi(update: Update, context: CallbackContext):
	update.message.reply_text("""
	""", parse_mode=ParseMode.HTML)

def jalur_prestasi(update: Update, context: CallbackContext):
	update.message.reply_text("""
	""", parse_mode=ParseMode.HTML)

def jalur_pto(update: Update, context: CallbackContext):
	update.message.reply_text("""
	""", parse_mode=ParseMode.HTML)

def peryaratan_ppdb(update: Update, context: CallbackContext):
	update.message.reply_text("""
    <b>UMUM</b>
    - Ijazah/Surat Keterangan Lulus/Kartu peserta Ujian Sekolah
    - Akta Kelahiran/Surat Keterangan Lahir
    - Kartu Keluarga (minimal satu tahun), KTP
    - Buku Rapor (semester 1 s.d. 5)
    - Surat Tanggung Jawab Mutlak Orang Tua\n\n<b>KHUSUS</b>
    - Kartu Program Penanganan Kemiskinan/Terdaftar pada DTKS Dinsos (bagi jalur - afirmasi/KETM)
    - Surat Keterangan Domisili dari RT/RW (bagi afirmasi korban bencana alam/sosial)
    - Surat Tugas Orangtua (bagi jalur perpindahan tugas orangtua/wali, maks. 3 tahun/anak guru)
    - Surat keputusan satgas covid bagi afirmasi kondisi tertentu penanganan Covid-19
    - Piagam dan Dokumentasi Prestasi (untuk jalur prestasi kejuaraan) maks. 5 tahun, min. 6 bulan
	""", parse_mode=ParseMode.HTML)

def unknown(update: Update, context: CallbackContext):
    update.message.reply_text("Maaf, perintah tidak dikenali. Silakan gunakan perintah yang valid." % update.message.text)

def unknown_text(update: Update, context: CallbackContext):
	update.message.reply_text(
		"Maaf, perintah tidak dikenali, '%s'" % update.message.text)


updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(MessageHandler(Filters.regex(r'(?i)^bantuan$'), bantuan))
updater.dispatcher.add_handler(MessageHandler(Filters.regex(r'(?i)^persyaratan_ppdb$'), peryaratan_ppdb))
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown))
updater.dispatcher.add_handler(MessageHandler(
	Filters.command, unknown)) # Filters out unknown commands

# Filters out unknown messages.
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown_text))

updater.start_polling()
