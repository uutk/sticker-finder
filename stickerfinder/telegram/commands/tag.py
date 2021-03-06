"""Tag related commands."""
from telegram.ext import run_async

from stickerfinder.helper.session import session_wrapper
from stickerfinder.helper.tag_mode import TagMode
from stickerfinder.helper.tag import handle_next, tag_sticker
from stickerfinder.models import Sticker


@run_async
@session_wrapper(check_ban=True)
def tag_single(bot, update, session, chat, user):
    """Tag the last sticker send to this chat."""
    # The tag command has been replied to another message
    # If it's a sticker, tags this specific sticker
    if (
        update.message.reply_to_message is not None
        and update.message.reply_to_message.sticker is not None
    ):
        tg_sticker = update.message.reply_to_message.sticker
        sticker = session.query(Sticker).get(tg_sticker.file_id)
        if sticker is None:
            return "This sticker has not yet been added."
        is_single_sticker = True

    # The tag command has been normally called
    elif chat.current_sticker:
        sticker = chat.current_sticker
        is_single_sticker = chat.tag_mode not in [TagMode.STICKER_SET, TagMode.RANDOM]
    else:
        return "No sticker for replacement selected"

    # Remove the /tag command
    text = update.message.text[4:]
    if text.strip() == "":
        return 'You need to add some tags to the /tag command. E.g. "/tag meme prequel obi wan"'

    tag_sticker(
        session,
        text,
        sticker,
        user,
        tg_chat=update.message.chat,
        chat=chat,
        message_id=update.message.message_id,
        single_sticker=is_single_sticker,
    )
    if not is_single_sticker:
        handle_next(session, bot, chat, update.message.chat, user)
    else:
        return "Sticker tags changed."


@run_async
@session_wrapper(check_ban=True)
def replace_single(bot, update, session, chat, user):
    """Tag the last sticker send to this chat."""
    # The replace command has been replied to another message
    # If it's a sticker, replace the tags of this specific sticker
    if (
        update.message.reply_to_message is not None
        and update.message.reply_to_message.sticker is not None
    ):
        tg_sticker = update.message.reply_to_message.sticker
        sticker = session.query(Sticker).get(tg_sticker.file_id)
        if sticker is None:
            return "This sticker has not yet been added."
        is_single_sticker = True

    # The replace command has been normally called
    elif chat.current_sticker:
        sticker = chat.current_sticker
        is_single_sticker = chat.tag_mode not in [TagMode.STICKER_SET, TagMode.RANDOM]
    else:
        return "No sticker for replacement selected"

    # Remove the /replace command
    text = update.message.text[8:]
    if text.strip() == "":
        return 'You need to add some tags to the /replace command. E.g. "/replace meme prequel obi wan"'

    tag_sticker(
        session,
        text,
        sticker,
        user,
        tg_chat=update.message.chat,
        chat=chat,
        message_id=update.message.message_id,
        single_sticker=is_single_sticker,
        replace=True,
    )
    if not is_single_sticker:
        handle_next(session, bot, chat, update.message.chat, user)
    else:
        return "Sticker tags replaced."
