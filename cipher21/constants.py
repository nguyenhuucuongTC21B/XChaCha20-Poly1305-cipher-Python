
KEY_LENGTH = 32

STREAM_SIGNATURE = b'c21\x1A\x00\xFF\x19\x82'

NONCE_OFFSET = len(STREAM_SIGNATURE)
NONCE_LENGTH = 24

TIMESTAMP_OFFSET = NONCE_OFFSET + NONCE_LENGTH
TIMESTAMP_LENGTH = 8

STREAM_LENGTH_MULTIPLICAND = 2**14
M = STREAM_LENGTH_MULTIPLICAND

PADDING_LENGTH_LENGTH = 2
assert 256**PADDING_LENGTH_LENGTH >= STREAM_LENGTH_MULTIPLICAND

MAC_LENGTH = 16

STREAM_HEADER_LENGTH = len(STREAM_SIGNATURE) + NONCE_LENGTH + TIMESTAMP_LENGTH

STREAM_FOOTER_LENGTH = PADDING_LENGTH_LENGTH + MAC_LENGTH

STREAM_METADATA_LENGTH = STREAM_HEADER_LENGTH + STREAM_FOOTER_LENGTH

