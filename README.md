# Web-Development

![HTML](images/HTML-tutorial.jpg)

<details>
<summary><b>HTML Introduction</b></summary>

## <b>Introduction:</b>

HTML stand for "Hyper Text Markup Language". HTML is the standard markup language used to create and design web pages. It provides a set of codes or tags that are used to structure the content of a webpage, such as text, images, links, and other elements. 

### <b>Start with HTML:</b>
---

+ <b>Choose Code Editor:</b>
  + Popular choices include Visual Studio Code, Sublime Text, Atom, and Notepad++.
  + Ensure that we have a web browser installed to preview our HTML pages. Popular choices include Google Chrome, Mozilla Firefox, and Microsoft Edge. HTML page always run on the web browser.
+ <b>Create a New File:</b></br>
  Create a new file and save it with a <code>.html </code> extension. For example, <code>index.html</code>
+ <b>Create the HTML Structure:</b>

<b>HTML Example:</b>

![HTML](images/HTML-Structure.png)

```html
<!DOCTYPE html>
<html>
<head>
    <title>Page Title</title>
</head>

<body>
    <h1>My First Heading</h1>
    <p>My first paragraph.</p>
</body>

</html>
```

</details>

<details>
<summary><b>HTML Tags</b></summary>

+ <code>Paragraph `<p>` Tag:</code> It's used to defines a paragraph of text.

    ```html
    <p>This is a paragraph of text.</p>
    ```

+ <code>Heading `<h1>` to `<h6>` Tags:</code> Defines headings of various levels, where `<h1>` is the highest level and `<h6>` is the lowest.
  
  ```html
    <h1>This is a level 1 heading</h1>
    <h2>This is a level 2 heading</h2>
    <h3>This is a level 3 heading</h3>
    <h4>This is a level 4 heading</h4>
    <h5>This is a level 5 heading</h5>
    <h6>This is a level 6 heading</h6>
  ```

+ <code>Break `<br>` Tag:</code> The `<br>` tags is used to insert a single line break. It does not have any closing tag.
  
  ```html
    <p>This is a line of text.</p>
    <p>This is another line of text.<br>This line will appear on a new line.</p>
  ```

+ <code>Anchor `<a>` Tag:</code> Defines a hyperlink, linking to another webpage or resource.
  
  ```html
    <a href="https://www.website.com">Visit Website</a>
  ```

+ <code>Image `<img>` Tag:</code> Embeds an image into the webpage.
  
  ```html
    <img src="image.jpg" alt="Description of image">
  ```
+ <code>Division `<div>` Tag:</code> Defines a division or section within a document, often used for layout purposes.
  
  ```html
    <div>
        <p>This is inside a division.</p>
    </div>
  ```

+ <code>Span `<span>` Tag:</code> Defines a section in a document that does not have any semantic meaning.
  
  ```html
    <p>This is <span style="color: red;">highlighted</span> text.</p>
  ```

+ <code>Form `<form>` Tag:</code> Defines an HTML form for user input.
  
  ```html
    <form action="/submit-form" method="post">
        <label for="username">Username:</label>
        <input type="text" id="username" name="username">
        <button type="submit">Submit</button>
    </form>
  ```

</details>