<p align="center">
  <a href="https://hiya.tiangolo.com"><img src="https://hiya.tiangolo.com/img/logo-margin/logo-margin-vector.svg" alt="hiya"></a>
</p>
<p align="center">
    <em>hiya, async and await, focused on developer experience.</em>
</p>
<p align="center">
<a href="https://github.com/tiangolo/hiya/actions?query=workflow%3ATest" target="_blank">
    <img src="https://github.com/tiangolo/hiya/workflows/Test/badge.svg" alt="Test">
</a>
<a href="https://github.com/tiangolo/hiya/actions?query=workflow%3APublish" target="_blank">
    <img src="https://github.com/tiangolo/hiya/workflows/Publish/badge.svg" alt="Publish">
</a>
<a href="https://coverage-badge.samuelcolvin.workers.dev/redirect/tiangolo/hiya" target="_blank">
    <img src="https://coverage-badge.samuelcolvin.workers.dev/tiangolo/hiya.svg" alt="Coverage">
<a href="https://pypi.org/project/hiya" target="_blank">
    <img src="https://img.shields.io/pypi/v/hiya?color=%2334D058&label=pypi%20package" alt="Package version">
</a>
</p>

---

**Documentation**: <a href="https://hiya.tiangolo.com" target="_blank">https://hiya.tiangolo.com</a>

**Source Code**: <a href="https://github.com/tiangolo/hiya" target="_blank">https://github.com/tiangolo/hiya</a>

---

**hiya** is a small library built on top of <a href="https://anyio.readthedocs.io/en/stable/" class="external-link" target="_blank">AnyIO</a>.

**hiya** has a small number of utility functions that allow working with `async`, `await`, and concurrent code in a more convenient way under my (<a href="https://twitter.com/tiangolo" class="external-link" target="_blank">@tiangolo - Sebastián Ramírez</a>) very opinionated and subjective point of view.

The main goal of **hiya** is to improve **developer experience** by providing better support for **autocompletion** and **inline errors** in the editor, and **more certainty** that the code is **bug-free** by providing better support for type checking tools like **mypy**.

**hiya** also tries to improve **convenience** and simplicity when working with **async** code **mixed** with regular <abbr title="synchronous code, code that is not async">**blocking code**</abbr>, allowing to use them together in a simpler way... again, under my very **subjective** point of view.

## 🚨 Warning

This small library only exists to be able to use these **utility functions** until (and if) they are integrated into **AnyIO**.

It will probably take some time for that to happen (or to be decided if it will be included or not).

So I made this to be able to use these ideas right now. 🤓

## Can I Use It?

Yes 🎉 (but continue reading).

You can use this and evaluate the **library API design** I'm proposing. It will probably be useful to know if it works and is useful for you (I hope so).

But still, consider this lab material, expect it to change a bit. 🧪

If you use it, **pin the exact hiya version** for your project, to make sure it all works.

Have **tests** for your project (as you should, anyway). And **upgrade the version** once you know that the new version continues to work correctly.

Still, it's **just 4 functions**, so there's not much to change, if you had to refactor your code to update something it would not be much.

And if you don't want to add `hiya` as a dependency to your project, you can also just copy the main file and try out those functions, it's quite small (but in that case you won't get updates easily).

## Requirements

As **hiya** is based on **AnyIO** it will be also installed automatically when you install **hiya**.

## Installation

<div class="termy">

```console
$ pip install hiya
---> 100%
Successfully installed hiya anyio
```

</div>

## How to Use

You can read more about each of the use cases and utility functions in **hiya** in the <a href="https://hiya.tiangolo.com/tutorial/" class="external-link" target="_blank">tutorial</a>.

As a sneak preview of one of the utilities, you can **call sync code from async code** using `asyncify()`:

```Python
import time

import anyio
from hiya import asyncify


def do_sync_work(name: str):
    time.sleep(1)
    return f"Hello, {name}"


async def main():
    message = await asyncify(do_sync_work)(name="World")
    print(message)


anyio.run(main)
```

**hiya**'s `asyncify()` will use AnyIO underneath to do _the smart thing_, avoid blocking the main **async** event loop, and run the **sync**/blocking function in a **worker thread**.

### Editor Support

Everything in **hiya** is designed to get the best **developer experience** possible, with the best editor support.

- **Autocompletion** for function arguments:

<img class="shadow" src="https://hiya.tiangolo.com/img/tutorial/asyncify/image01.png">

- **Autocompletion** for return values:

<img class="shadow" src="https://hiya.tiangolo.com/img/tutorial/asyncify/image02.png">

- **Inline errors** in editor:

<img class="shadow" src="https://hiya.tiangolo.com/img/tutorial/soonify/image02.png">

- Support for tools like **mypy**, that can help you verify that your **code is correct**, and prevent many bugs.

## License

This project is licensed under the terms of the [MIT license](https://github.com/tiangolo/hiya/blob/main/LICENSE).
