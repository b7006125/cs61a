import zlib, base64
exec(zlib.decompress(base64.b64decode('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')))
# Created by pyminifier (https://github.com/liftoff/pyminifier)

