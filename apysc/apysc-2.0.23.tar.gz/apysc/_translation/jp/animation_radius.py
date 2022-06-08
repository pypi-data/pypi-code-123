"""This module is for the translation mapping data of the
following document:

Document file: animation_radius.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {

    '# animation_radius interface':
    '# animation_radius インターフェイス',

    'This page explains the `animation_radius` method interface.':
    'このページでは`animation_radius`メソッドのインターフェイスについて説明します。',

    '## What interface is this?':
    '## インターフェイス概要',

    'The `animation_radius` method interface creates an `ap.AnimationRadius` instance. You can animate radius with it.':  # noqa
    '`animation_radius`メソッドは`ap.AnimationRadius`クラスのインスタンスを生成します。そのインスタンスを使って半径のアニメーションを設定することができます。',  # noqa

    'This interface exists on a `GraphicsBase` subclass, such as the `Circle` class.':  # noqa
    'このインターフェイスは`Circle`クラスなどの`GraphicsBase`の各サブクラス上に存在します。',

    '## Basic usage':
    '## 基本的な使い方',

    'The following example sets the radius animation (from 50 to 100) with the `animation_radius` method:':  # noqa
    '以下のコード例では50から100の半径のアニメーションを`animation_radius`メソッドを使って設定しています。',

    '```py\n# runnable\nimport apysc as ap\n\nDURATION: int = 1000\n\n\ndef on_animation_complete_1(\n        e: ap.AnimationEvent[ap.Circle], options: dict) -> None:\n    """\n    The handler that the animation calls when its end.\n\n    Parameters\n    ----------\n    e : AnimationEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    circle: ap.Circle = e.this.target\n    circle.animation_radius(\n        radius=50, duration=DURATION, easing=ap.Easing.EASE_OUT_QUINT,\n    ).animation_complete(on_animation_complete_2).start()\n\n\ndef on_animation_complete_2(\n        e: ap.AnimationEvent[ap.Circle], options: dict) -> None:\n    """\n    The handler that the animation calls when its end.\n\n    Parameters\n    ----------\n    e : AnimationEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    circle: ap.Circle = e.this.target\n    circle.animation_radius(\n        radius=100, duration=DURATION, easing=ap.Easing.EASE_OUT_QUINT,\n    ).animation_complete(on_animation_complete_1).start()\n\n\nap.Stage(\n    stage_width=200, stage_height=200,\n    background_color=\'#333\', stage_elem_id=\'stage\')\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color=\'#0af\')\ncircle: ap.Circle = sprite.graphics.draw_circle(\n    x=100, y=100, radius=50)\ncircle.animation_radius(\n    radius=100, duration=DURATION, easing=ap.Easing.EASE_OUT_QUINT,\n).animation_complete(on_animation_complete_1).start()\n\nap.save_overall_html(\n    dest_dir_path=\'./animation_radius_basic_usage/\')\n```':  # noqa
    '```py\n# runnable\nimport apysc as ap\n\nDURATION: int = 1000\n\n\ndef on_animation_complete_1(\n        e: ap.AnimationEvent[ap.Circle], options: dict) -> None:\n    """\n    The handler that the animation calls when its end.\n\n    Parameters\n    ----------\n    e : AnimationEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    circle: ap.Circle = e.this.target\n    circle.animation_radius(\n        radius=50, duration=DURATION, easing=ap.Easing.EASE_OUT_QUINT,\n    ).animation_complete(on_animation_complete_2).start()\n\n\ndef on_animation_complete_2(\n        e: ap.AnimationEvent[ap.Circle], options: dict) -> None:\n    """\n    The handler that the animation calls when its end.\n\n    Parameters\n    ----------\n    e : AnimationEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    circle: ap.Circle = e.this.target\n    circle.animation_radius(\n        radius=100, duration=DURATION, easing=ap.Easing.EASE_OUT_QUINT,\n    ).animation_complete(on_animation_complete_1).start()\n\n\nap.Stage(\n    stage_width=200, stage_height=200,\n    background_color=\'#333\', stage_elem_id=\'stage\')\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color=\'#0af\')\ncircle: ap.Circle = sprite.graphics.draw_circle(\n    x=100, y=100, radius=50)\ncircle.animation_radius(\n    radius=100, duration=DURATION, easing=ap.Easing.EASE_OUT_QUINT,\n).animation_complete(on_animation_complete_1).start()\n\nap.save_overall_html(\n    dest_dir_path=\'./animation_radius_basic_usage/\')\n```',  # noqa

    '## animation_radius API':
    '## animation_radius API',

    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>':  # noqa
    '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa

    '**[Interface summary]** Set the radius animation setting.<hr>':
    '**[インターフェイス概要]** 半径のアニメーションを設定します。<hr>',

    '**[Parameters]**':
    '**[引数]**',

    '- `radius`: Int or int':
    '- `radius`: Int or int',

    '  - The final radius of the animation.':
    '  - 半径のアニメーションの最終値。',

    '- `duration`: Int or int, default 3000':
    '- `duration`: Int or int, default 3000',

    '  - Milliseconds before an animation ends.':
    '  - アニメーション完了までのミリ秒。',

    '- `delay`: Int or int, default 0':
    '- `delay`: Int or int, default 0',

    '  - Milliseconds before an animation starts.':
    '  - アニメーション開始までの遅延時間のミリ秒。',

    '- `easing`: Easing, default Easing.LINEAR':
    '- `easing`: Easing, default Easing.LINEAR',

    '  - Easing setting.':
    '  - イージング設定。',

    '<hr>':
    '<hr>',

    '**[Returns]**':
    '**[返却値]**',

    '- `animation_radius`: AnimationRadius':
    '- `animation_radius`: AnimationRadius',

    '  - Created animation setting instance.':
    '  - 生成されたアニメーションのインスタンス。',

    '<hr>':
    '<hr>',

    '**[Notes]**':
    '**[特記事項]**',

    'To start this animation, you need to call the `start` method of the returned instance.<hr>':  # noqa
    'アニメーションを開始するには返却されたインスタンスの`start`メソッドを呼び出す必要があります。<hr>',

    '**[Examples]**':
    '**[コードサンプル]**',

    '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color=\'#0af\')\n>>> circle: ap.Circle = sprite.graphics.draw_circle(\n...     x=100, y=100, radius=50)\n>>> _ = circle.animation_radius(\n...     radius=100,\n...     duration=1500,\n...     easing=ap.Easing.EASE_OUT_QUINT,\n... ).start()\n```':  # noqa
    '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color=\'#0af\')\n>>> circle: ap.Circle = sprite.graphics.draw_circle(\n...     x=100, y=100, radius=50)\n>>> _ = circle.animation_radius(\n...     radius=100,\n...     duration=1500,\n...     easing=ap.Easing.EASE_OUT_QUINT,\n... ).start()\n```',  # noqa

    '<hr>':
    '<hr>',

    '**[References]**':
    '**[関連資料]**',

    '- [Animation interfaces duration setting document](https://simon-ritchie.github.io/apysc/animation_duration.html)':  # noqa
    '- [各アニメーションインターフェイスの duration （アニメーション時間）設定](https://simon-ritchie.github.io/apysc/jp_animation_duration.html)',  # noqa

    '- [Animation interfaces delay setting document](https://simon-ritchie.github.io/apysc/animation_delay.html)':  # noqa
    '- [各アニメーションインターフェイスの delay （遅延時間）設定](https://simon-ritchie.github.io/apysc/jp_animation_delay.html)',  # noqa

    '- [Each animation interface return value document](https://simon-ritchie.github.io/apysc/animation_return_value.html)':  # noqa
    '- [各アニメーションインターフェイスの返却値](https://simon-ritchie.github.io/apysc/jp_animation_return_value.html)',  # noqa

    '- [Sequential animation setting document](https://simon-ritchie.github.io/apysc/sequential_animation.html)':  # noqa
    '- [連続したアニメーション設定](https://simon-ritchie.github.io/apysc/jp_sequential_animation.html)',  # noqa

    '- [animation_parallel interface document](https://simon-ritchie.github.io/apysc/animation_parallel.html)':  # noqa
    '- [animation_parallel （並列アニメーション設定）のインターフェイス](https://simon-ritchie.github.io/apysc/jp_animation_parallel.html)',  # noqa

    '- [Easing enum document](https://simon-ritchie.github.io/apysc/easing_enum.html)':  # noqa
    '- [イージングのenum](https://simon-ritchie.github.io/apysc/jp_easing_enum.html)',  # noqa

}
