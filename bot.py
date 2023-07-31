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
	<b>Seputar ppdb</b> - Berisi informasi umum mengenai PPDB
	<b>Persyaratan ppdb</b> - Berisi persyaratan PPDB
	""", parse_mode=ParseMode.HTML)


def seputar_ppdb(update: Update, context: CallbackContext):
	update.message.reply_text("""
	Seputar PPDB
	Kata Kunci Tersedia :
	<b>Jalur ppdb</b> - Berisi informasi jalur yang tersedia
	<b>Nilai prestasi</b> - Berisi informasi Nilai tambahan
	<b>Daftar ulang</b> - Berisi informasi Daftar ulang
	""", parse_mode=ParseMode.HTML)


def jalur_ppdb(update: Update, context: CallbackContext):
	update.message.reply_text("""
	Jalur PPDB
	Kata Kunci Tersedia :
	<b>Jalur zonasi</b> - Berisi informasi jalur Zonasi
	<b>Jalur afirmasi</b> - Berisi informasi jalur aformasi
	<b>Jalur prestasi</b> - Berisi informasi jalur Prestasi
	<b>Jalur pto</b> - Berisi informasi jalur pto
	""", parse_mode=ParseMode.HTML)

def daftar_ulang(update: Update, context: CallbackContext):
	update.message.reply_text("""
	""", parse_mode=ParseMode.HTML)

def nilai_prestasi(update: Update, context: CallbackContext):
	update.message.reply_text("""
	""", parse_mode=ParseMode.HTML)

def jalur_zonasi(update: Update, context: CallbackContext):
	update.message.reply_text("""
	Jalur zonasi adalah salah satu jalur dalam PPDB SMA dan SMK Negeri yang salah satu komponen seleksinya didasarkan pada domisili atau zona calon peserta didik baru. Kuota jalur zonasi sebesar 55% (lima puluh lima) dari daya tampung sekolah yang terbagi menjadi 5% (lima persen) zonasi radius dan 50% (lima puluh persen) zonasi reguler.
	""", parse_mode=ParseMode.HTML)

def jalur_afirmasi(update: Update, context: CallbackContext):
	update.message.reply_text("""
	Jalur afirmasi adalah jalur PPDB yang diperuntukkan bagi:
	a. Calon peserta didik dari keluarga ekonomi tidak mampu.
	b. Calon peserta didik penyandang disabilitas pada sekolah yang menyelenggarakan pendidikan inklusif.
	Jalur afirmasi memiliki kuota sebesar 20% (dua puluh persen) dari daya tampung sekolah.
	""", parse_mode=ParseMode.HTML)

def jalur_prestasi(update: Update, context: CallbackContext):
	update.message.reply_text("""
	Jalur prestasi merupakan jalur khusus untuk peserta didik dengan nilai gabungan minimal sebesar 330 (tiga ratus tiga puluh). Kuota jalur prestasi sebesar 20% (dua puluh persen) dari daya tampung sekolah.
	""", parse_mode=ParseMode.HTML)

def jalur_pto(update: Update, context: CallbackContext):
	update.message.reply_text("""
	Jalur PTO diperuntukkan bagi calon peserta didik yang berdomisili di luar Zonasi Sekolah yang bersangkutan, dimana meliputi:
	1. Perpindahan tugas Orang Tua/Wali dari luar DIY ke dalam DIY, dibuktikan dengan Kartu Keluarga luar DIY.
	2. Perpindahan tugas Orang Tua/Wali antar Kabupaten/Kota dalam DIY yang diikuti perpindahan domisili Orang Tua/Wali, yang dibuktikan dengan perpindhan Kartu Keluarga, Surat perpindahan tugas.
	Jalur PTO memiliki daya tampung sebesar 5% (lima persen) dari daya tampung sekolah.
	""", parse_mode=ParseMode.HTML)

def peryaratan_ppdb(update: Update, context: CallbackContext):
	update.message.reply_text("""
    <b>UMUM</b>
    Ijazah/Surat Keterangan Lulus/Kartu peserta Ujian Sekolah
    Akta Kelahiran/Surat Keterangan Lahir
    Kartu Keluarga (minimal satu tahun)
	Buku Rapor (semester 1 s.d. 5)
    Surat Tanggung Jawab Mutlak Orang Tua\n\n<b>KHUSUS</b>
    Kartu Program Penanganan Kemiskinan/Terdaftar pada DTKS Dinsos (bagi jalur - afirmasi/KETM)
    Surat Keterangan Domisili dari RT/RW (bagi afirmasi korban bencana alam/sosial)
    Surat Tugas Orangtua (bagi jalur perpindahan tugas orangtua/wali, maks. 3 tahun/anak guru)
    Surat keputusan satgas covid bagi afirmasi kondisi tertentu penanganan Covid-19
    Piagam dan Dokumentasi Prestasi (untuk jalur prestasi kejuaraan) maks. 5 tahun, min. 6 bulan
	""", parse_mode=ParseMode.HTML)

def unknown(update: Update, context: CallbackContext):
    update.message.reply_text("Maaf, perintah tidak dikenali. Silakan gunakan perintah yang valid." % update.message.text)

def unknown_text(update: Update, context: CallbackContext):
	update.message.reply_text(
		"Maaf, perintah tidak dikenali, '%s'" % update.message.text)


updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(MessageHandler(Filters.regex(r'(?i)^bantuan$'), bantuan))
updater.dispatcher.add_handler(MessageHandler(Filters.regex(r'(?i)^jalur ppdb$'), jalur_ppdb))
updater.dispatcher.add_handler(MessageHandler(Filters.regex(r'(?i)^seputar ppdb$'), seputar_ppdb))
updater.dispatcher.add_handler(MessageHandler(Filters.regex(r'(?i)^daftar ulang$'), daftar_ulang))
updater.dispatcher.add_handler(MessageHandler(Filters.regex(r'(?i)^nilai prestasi$'), nilai_prestasi))
updater.dispatcher.add_handler(MessageHandler(Filters.regex(r'(?i)^jalur zonasi$'), jalur_zonasi))
updater.dispatcher.add_handler(MessageHandler(Filters.regex(r'(?i)^jalur afirmasi$'), jalur_afirmasi))
updater.dispatcher.add_handler(MessageHandler(Filters.regex(r'(?i)^jalur prestasi$'), jalur_prestasi))
updater.dispatcher.add_handler(MessageHandler(Filters.regex(r'(?i)^jalur pto$'), jalur_pto))
updater.dispatcher.add_handler(MessageHandler(Filters.regex(r'(?i)^persyaratan ppdb$'), peryaratan_ppdb))
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown))
updater.dispatcher.add_handler(MessageHandler(Filters.command, unknown)) # Filters out unknown commands
# Filters out unknown messages.
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown_text))

updater.start_polling()
