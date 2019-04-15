"""Test the session test setup."""
from stickerfinder.helper.tag import tag_sticker
from tests.helper import assert_sticker_contains_tags


def test_add_tags(session, user, sticker_set):
    """Test adding new tags to a sticker."""
    for sticker in sticker_set.stickers:
        # Create a new tag for each sticker
        tag_sticker(session, f'tag_{sticker.file_id}', sticker, user)

    session.commit()

    # Ensure that the mallicious user actually replaced the tag
    for sticker in sticker_set.stickers:
        assert sticker.tags[0].name == f'tag_{sticker.file_id}'

    # User got a new change
    assert len(user.changes) == len(sticker_set.stickers)

    for sticker in sticker_set.stickers:
        # Create a new tag for each sticker
        tag_sticker(session, f'tag_2_{sticker.file_id}', sticker, user)

    session.commit()

    # Ensure that the mallicious user actually replaced the tag
    for sticker in sticker_set.stickers:
        assert_sticker_contains_tags(sticker, [f'tag_{sticker.file_id}', f'tag_2_{sticker.file_id}'])
    assert len(user.changes) == len(sticker_set.stickers) * 2


def test_replace_sticker_tags(session, user, sticker_set, tags):
    """Test replacing tags of a sticker."""
    for sticker in sticker_set.stickers:
        # Replace the existing tag
        tag_sticker(session, f'new_tag_{sticker.file_id}', sticker, user, replace=True)

    session.commit()

    # Ensure the tag has been replaced
    for sticker in sticker_set.stickers:
        assert len(sticker.tags) == 1
        assert sticker.tags[0].name == f'new_tag_{sticker.file_id}'

    assert len(user.changes) == len(sticker_set.stickers) * 2
