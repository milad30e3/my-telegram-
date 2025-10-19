import telebot # 'Import' কে 'import' করা হয়েছে, যা প্রধান এরর দূর করবে
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

# আপনার টোকেন
TOKEN = "8479459644:AAEZS-iLIgCZbBH7PyMbYkfnWAnKPidcfAA"
bot = telebot.TeleBot(TOKEN)

GROUP_LINK = "https://t.me/bangladeshideshivideo"
YOUTUBE_LINK = "https://www.youtube.com/@Deshiviralvideo30"

# /start কমান্ডের জন্য হ্যান্ডলার
@bot.message_handler(commands=['start'])
def start(message):
    markup = InlineKeyboardMarkup()
    
    # সাবস্ক্রাইব করার জন্য প্রথম বাটন
    subscribe_button = InlineKeyboardButton("Subscribe ✅", url=YOUTUBE_LINK)
    
    # সাবস্ক্রাইব করার পর গ্রুপ লিঙ্ক পাওয়ার জন্য দ্বিতীয় বাটন
    # 'callback_data' ব্যবহার করা হয়েছে, যা আরও সঠিক পদ্ধতি
    get_link_button = InlineKeyboardButton("Already Subscribed? Click Here", callback_data="get_group_link")
    
    markup.add(subscribe_button)
    markup.add(get_link_button)
    
    bot.send_message(
        message.chat.id, 
        "গ্রুপ লিঙ্ক পেতে, প্রথমে আমাদের ইউটিউব চ্যানেলটি Subscribe করুন এবং তারপর 'Already Subscribed? Click Here' বাটনে ক্লিক করুন:", 
        reply_markup=markup
    )

# নতুন ফাংশন: ইনলাইন বোতাম প্রেস করলে এই ফাংশনটি কাজ করবে
@bot.callback_query_handler(func=lambda call: call.data == "get_group_link")
def send_group_link(call):
    # ব্যবহারকারীকে নিশ্চিত করার জন্য একটি পপ-আপ মেসেজ পাঠানো
    bot.answer_callback_query(call.id, "ধন্যবাদ! গ্রুপ লিঙ্ক নিচে দেওয়া হলো।")
    
    # গ্রুপ লিঙ্ক পাঠানো
    bot.send_message(
        call.message.chat.id, 
        f"গ্রুপ লিঙ্ক: {GROUP_LINK}"
    )
    
    # ঐ মেসেজটি এডিট করে বাটনগুলো সরিয়ে দেওয়া (ঐচ্ছিক)
    bot.edit_message_text(
        "আপনাকে গ্রুপ লিঙ্ক দেওয়া হয়েছে।",
        call.message.chat.id,
        call.message.message_id
    )

# যেকোনো সাধারণ মেসেজের জন্য হ্যান্ডলার (যদি কেউ শুধু টেক্সট লেখে)
@bot.message_handler(func=lambda message: True)
def handle_general_message(message):
    # /start মেসেজ হলে এড়িয়ে যাবে
    if message.text != "/start":
        bot.send_message(
            message.chat.id, 
            "দয়া করে /start কমান্ড ব্যবহার করুন।"
        )


bot.polling(none_stop=True) # none_stop=True ব্যবহার করলে বট আরও স্থিতিশীল ভাবে চলবে