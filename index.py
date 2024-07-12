html = """
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Code Editor</title>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
    <link href="https://getbootstrap.com/docs/5.3/assets/css/docs.css" rel="stylesheet">
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700;900&display=swap" rel="stylesheet">
    <link rel="stylesheet"
        href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@48,400,0,0" />
    <link rel="stylesheet"
        href="https://fonts.googleapis.com/css2?family=Material+Symbols+Rounded:opsz,wght,FILL,GRAD@48,400,1,0" />
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/css/bootstrap.min.css" rel="stylesheet"
        integrity="sha384-Zenh87qX5JnK2Jl0vWa8Ck2rdkQ2Bzep5IDxbcnCeuOxjzrPF/et3URy9Bv1WTRi" crossorigin="anonymous">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.65.7/codemirror.min.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.65.7/theme/dracula.min.css">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.9.1/font/bootstrap-icons.css">
    <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.7.1/jquery.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/js/bootstrap.bundle.min.js"
        integrity="sha384-OERcA2EqjJCMA+/3y+gxIOqMEjwtxJY7qPCqsdltbNJuaOe923+mo//f6V8Qbsw3"
        crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.65.7/codemirror.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.65.7/mode/python/python.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.65.7/addon/edit/closebrackets.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.65.7/addon/hint/show-hint.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.65.7/addon/hint/python-hint.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/bootstrap-growl/1.0.0/jquery.bootstrap-growl.min.js"></script>
</head>

<body>
    <div class="row m-3">
        <div class="col">
            <div class="d-flex justify-content-between mb-2 bg-dark rounded p-2">
                <div class="col-12 w-25">
                    <label class="visually-hidden" for="inlineFormSelectPref">Preference</label>
                    <h5 style="color: aliceblue;margin-top: 6px;padding-left: 22px;width: 276px;">MicroPython Code
                        Editor</h5>
                </div>
                <div>
                    <button type="button" id="compileWeb" class="btn btn-success">Status</button>
                    <button type="button" id="run" class="btn btn-success"><i class="bi bi-play-fill"></i></button>
                </div>
            </div>
            <textarea id="editor" class="form-control" aria-label="Editor">{lastProgram}</textarea>
        </div>
        <div class="toast fade show" role="alert" aria-live="assertive" aria-atomic="true">
            <div class="toast-header">
                <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="currentColor" class="bi bi-bell"
                    viewBox="0 0 16 16">
                    <path
                        d="M8 16a2 2 0 0 0 2-2H6a2 2 0 0 0 2 2M8 1.918l-.797.161A4 4 0 0 0 4 6c0 .628-.134 2.197-.459 3.742-.16.767-.376 1.566-.663 2.258h10.244c-.287-.692-.502-1.49-.663-2.258C12.134 8.197 12 6.628 12 6a4 4 0 0 0-3.203-3.92zM14.22 12c.223.447.481.801.78 1H1c.299-.199.557-.553.78-1C2.68 10.2 3 6.88 3 6c0-2.42 1.72-4.44 4.005-4.901a1 1 0 1 1 1.99 0A5 5 0 0 1 13 6c0 .88.32 4.2 1.22 6" />
                </svg>
                <strong class="me-auto"><strong>Notification</strong></strong>
                <small class="text-body-secondary" id="timestamp">Just now</small>
                <button type="button" class="btn-close" data-bs-dismiss="toast" aria-label="Close"
                    fdprocessedid="y1tvmn"></button>
            </div>
            <div class="toast-body">
                <strong>MicroPython Web Code Editor</strong><br>
                The purpose of the MicroPython web code editor is to eliminate the need for physical IDE software. This web editor provides a high-speed program upload to the device and includes an inbuilt web server to host the MicroPython code editor webpage. It can handle uploading, debugging, and more.
                <br><br><b>Editor Options</b><br>
                The editor has two buttons: <strong>'Run'</strong> and <strong>'Status'</strong>
                <br><br>
                <ul>
                    <li><b>'Run'</b>: This button uploads the program to the corresponding device and checks for syntax errors only. Once the program is uploaded, wait a few seconds until the device's onboard LED turns off.</li>
                    <li><b>'Status'</b>: This button checks for error logs. If the previously uploaded program has runtime errors, they will be notified here.</li>
                </ul>
                <br><b>Shortcut Keys</b>
                <ul>
                    <li><b>Ctrl+u</b>, <b>F4</b>: Upload the program.</li>
                    <li><b>F2</b>: Check for error logs.</li>
                </ul>
            </div>
        </div>
    </div>
    <script>
        let growlNotification = null;

        function bootstrapAlert(message) {
            growlNotification = $.bootstrapGrowl(message, {
                type: "info",
                offset: { from: "top", amount: 250 },
                align: "center",
                delay: 3000,
                allow_dismiss: false,
                stackup_spacing: 10
            });
        }

        var editor = CodeMirror.fromTextArea(document.getElementById("editor"), {
            mode: "text/x-python",
            theme: "dracula",
            lineNumbers: true,
            autoCloseBrackets: true,
            extraKeys: { "Ctrl-Space": "autocomplete" },
            hintOptions: { completeSingle: false }
        });

        editor.setSize("100%", "600px");
        editor.setOption("mode", "text/x-python");
        editor.on("inputRead", function (cm, event) {
            if (event.origin === "paste") return;
            if (event.key && /^[a-zA-Z0-9_.,(){}[\]'"`]$/.test(event.key)) {
                CodeMirror.commands.autocomplete(cm, null, { completeSingle: false });
            }
        });

        async function handleAction(endpoint, alertMessage) {
            const code = editor.getValue();
            bootstrapAlert(alertMessage);

            try {
                const response = await fetch(`http://{ip}/${endpoint}`, {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json"
                    },
                    body: JSON.stringify({ code: code })
                });

                if (!response.ok) {
                    throw new Error(`HTTP error! Status: ${response.status}`);
                }

                const data = await response.json();
                bootstrapAlert(data.output);
                if (endpoint === "run") {
                    bootstrapAlert("Waiting for devices");
                }

            } catch (error) {
                console.error('Error:', error);
                bootstrapAlert('An error occurred');
            }
        }

        document.getElementById("compileWeb").addEventListener("click", function () {
            handleAction("compile", "Status checking...");
        });

        document.getElementById("run").addEventListener("click", function () {
            handleAction("run", "Uploading....");
        });
        document.addEventListener("keydown", e => {
            if (
                (e.key === "u"
                    && e.ctrlKey) || (e.key === "F4")
            ) {
                handleAction("run", "Uploading....");
            } else if (
                e.key === "F2"
            ) {
                handleAction("compile", "Status checking...");
            }
        })
        alert("Welcome to Micropython Code Editor");
        function updateTime() {
            const timestampElement = document.getElementById('timestamp');
            const now = new Date();
            const minutesElapsed = Math.floor((now - startTime) / 60000);

            if (minutesElapsed === 0) {
                timestampElement.textContent = "Just now";
            } else if (minutesElapsed === 1) {
                timestampElement.textContent = "1 min ago";
            } else {
                timestampElement.textContent = `${minutesElapsed} mins ago`;
            }
        }

        const startTime = new Date();
        updateTime();
        setInterval(updateTime, 60000);
    </script>
</body>

</html>
"""

backup = 'import freeIDE\n\nSSID = "vivoY12G"\nPassword = "raghulrajg"\n\nclient = freeIDE.FreeIDE(SSID, Password)\n\ndef loop():\n    while True:\n        #put your code here\n        pass\n        \nif __name__ == \'__main__\':\n    loop()'
