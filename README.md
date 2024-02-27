# Learning Web-Development

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

### HTML Tags
---

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

<details>
<summary><b>HTML Attributes</b></summary>

### HTML Attributes
---

1. `**id**`: Specifies a unique identifier for an element.
   
   ```html
    <div id="header">...</div>
   ```

2. `**class**:` Specifies one or more class names for an element (used for styling with CSS).
   
   ```html
    <p class="highlighted">...</p>
   ```

3. `**style**:` Specifies inline CSS styles for an element.
   
   ```html
    <h1 style="color: blue; font-size: 24px;">...</h1>
   ```

4. `**href**:` Specifies the URL of a link.
   
   ```html
    <a href="https://www.example.com">Link</a>
   ```

5. `**src**:` Specifies the URL of an image or other external resource.
   
   ```html
    <img src="image.jpg" alt="Description">
   ```

6. `**alt**:` Specifies alternative text for an image (useful for accessibility).
   
   ```html
    <img src="image.jpg" alt="Description">
   ```

7. `**title**:` Specifies additional information about an element (often displayed as a tooltip).
   
   ```html
    <p title="I'm a tooltip">This is a paragraph.</p>
   ```

8. `**width** and **height**:` Specifies the width and height of an element (such as an image).
   
   ```html
    <img src="image.jpg" alt="Description" width="200px" height="150px">
   ```

9.  `**target**:` Specifies where to open the linked document when clicked (e.g., `_blank` to open in a new tab).
    
    ```html
    <a href="https://www.example.com" target="_blank">Link</a>
    ```

10. `**rel**:` Specifies the relationship between the current document and the linked document (e.g., `stylesheet` for a CSS file).
    
    ```html
    <link rel="stylesheet" href="styles.css">
    ```

11. `**type**:` Specifies the media type of the linked document (e.g., `text/css` for a CSS file).
    
    ```html
    <link rel="stylesheet" type="text/css" href="styles.css">
    ```

12. `**disabled**:` Disables an input element or button.
    
    ```html
    <input type="submit" value="Submit" disabled>
    ```

13. `**readonly**:` Specifies that an input field is read-only (cannot be edited).
    
    ```html
    <input type="text" value="Read-only text" readonly>
    ```
14. `**lang**:` We should always include the lang attribute inside the `<html>` tag, to declare the language of the Web page.
    
    ```html
    <html lang="en">
    ```


</details>

<details>
<summary><b>Text Formatting</b></summary>

1. `<b> - Bold text:`
   This element defines bold text, without any extra importance.

   ```html
    <p>This is <b>bold</b> text.</p>
   ```

2. `<strong> - Important text:`
   This element defines text with strong importance. The content inside is typically displayed in bold.

   ```html
    <p>This is <strong>important</strong> text.</p>
   ```

3. `<i> - Italic text:`
   Renders text in italic.

   ```html
    <p>This is <i>italic</i> text.</p>
   ```

4. `<em> - Emphasized text:`
   Renders text in italic, typically indicating emphasis.

   ```html
    <p>This is <em>emphasized</em> text.</p>
   ```

5. `<mark> - Marked text:`
   Renders text with a background color, typically indicating relevance or highlighted text.

   ```html
    <p>This is <mark>highlighted</mark> text.</p>
   ```

6. `<small> - Smaller text:`
   Renders text in a smaller font size.

   ```html
    <p>This is <small>smaller</small> text.</p>
   ```

7. `<del> - Deleted text:`
   Renders text with a strikethrough, indicating deleted content.

   ```html
    <p>This is <del>deleted</del> text.</p>
   ```

8. `<ins> - Inserted text:`
   Renders text with an underline, indicating inserted content.

   ```html
    <p>This is <ins>inserted</ins> text.</p>
   ```

9. `<sub> - Subscript text:`
   Renders text as a subscript (below the baseline).

   ```html
    <p>This is H<sub>2</sub>O text.</p>
   ```

10. `<sup> - Superscript text:`
    Renders text as a superscript (above the baseline).

    ```html
    <p>This is 10<sup>2</sup> text.</p>
    ```


</details>