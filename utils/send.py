import fluxer

async def send(ctx, *, content=None, embed=None, embeds=None, **kwargs):
    # Handle single embed
    if embed is not None:
        if isinstance(embed, fluxer.Embed):
            embeds = [embed.to_dict()]
        else:
            embeds = [embed]

    # Handle multiple embeds
    if embeds is not None:
        fixed = []
        for e in embeds:
            if isinstance(e, fluxer.Embed):
                fixed.append(e.to_dict())
            else:
                fixed.append(e)
        embeds = fixed

    return await ctx.send(content=content, embeds=embeds, **kwargs)
