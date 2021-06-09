import React, {useState} from "react";
import TopBar from "../../components/TopBar";
import {Button, Card, createStyles, Grid, makeStyles, TextField, Typography} from "@material-ui/core";
import axios from "axios";
import {handleAxiosError} from "../../utils/AxiosUtils";
import {useSnackbar} from "notistack";
import CircularProgress from '@material-ui/core/CircularProgress';

const useStyles = makeStyles((theme) =>
    createStyles({
        container: {
            height: "100%",
            flex: 1,
            display: "flex",
            justifyContent: "space-evenly",
            alignItems: "center",
            marginTop: "50px",
            [theme.breakpoints.down("sm")]: {
                flexDirection: "column",
            },
            [theme.breakpoints.up("md")]: {
                flexDirection: "row",
            },
        },
        card: {
            height: "80%",
            width: "80%",
            display: "flex",
            flexDirection: "column",
            justifyContent: "space-evenly",
            padding: 8,
            marginTop: 50
        },
        text: {
            textAlign: "center",
            [theme.breakpoints.only("xs")]: {
                fontSize: "1rem",
            },
            [theme.breakpoints.only("sm")]: {
                fontSize: "1.25rem",
            },
            [theme.breakpoints.only("md")]: {
                fontSize: "1.5rem",
            },
            [theme.breakpoints.up("lg")]: {
                fontSize: "2rem",
            },
        },
        button: {
            height: "60px",
            width: "150px",
            fontSize: "2rem",
        },
        buttonContainer: {
            justifyContent: "center",
            alignItems: "center",
            display: "flex",
        },
        typography: {
            whiteSpace: "pre-line"
        }
    })
);

const axiosConfig = {headers: {"content-type": "multipart/form-data"}};

const Detection: React.FC = () => {

    const [text, setText] = useState("");
    const [error, setError] = useState(false);
    const [results, setResults] = useState("");
    const [evaluating, setEvaluating] = useState(false);

    const {enqueueSnackbar} = useSnackbar();

    const onTextChange = (event: React.ChangeEvent<HTMLInputElement>) => {
        setError(false);
        setText(event.target.value);
    };

    const onCheckClick = () => {
        if (text === "") {
            setError(true);
        } else {
            setEvaluating(true)
            const formData = new FormData();
            formData.append("text", text);
            axios
                .post("https://individual-project-app.herokuapp.com/result/", formData, axiosConfig)
                .then((response) => {
                    const success = response.status === 200;

                    if (success) {
                        setResults(response.data)
                        console.log(response.data)
                    }

                    /* Enqueue snackbar with the Server Response */
                    const responseSnackbarOptions = success
                        ? {
                            anchorOrigin: {
                                vertical: "bottom",
                                horizontal: "left",
                            },
                            autoHideDuration: 6000,
                            variant: "success",
                        }
                        : {
                            anchorOrigin: {
                                vertical: "bottom",
                                horizontal: "right",
                            },
                            autoHideDuration: 3000,
                            variant: "error"
                        };

                    // @ts-ignore
                    enqueueSnackbar("Evaluation Finished", responseSnackbarOptions);
                    setEvaluating(false)
                })
                .catch((error) => {
                    if (axios.isAxiosError(error)) {
                        handleAxiosError(error);

                        if (error.response) {

                            /* Enqueue snackbar with the Server Error */
                            enqueueSnackbar(error.response.data, {
                                anchorOrigin: {
                                    vertical: "bottom",
                                    horizontal: "right",
                                },
                                autoHideDuration: 3000,
                                variant: "error"
                            });
                        }
                    }
                });
        }
    }

    const classes = useStyles();

    return (
        <>
            <TopBar showBack/>
            <Grid
                container
                direction="column"
                justify="space-evenly"
                alignItems="center"
            >
                <Card className={classes.card}>
                    <Typography className={classes.text}>
                        In the box below you can enter the text that you want to evaluate
                    </Typography>
                    <TextField
                        margin="dense"
                        label="Insert your text here"
                        required
                        size="medium"
                        multiline
                        type="text"
                        error={error}
                        helperText={error ? "Text box cannot be empty" : ""}
                        value={text}
                        onChange={onTextChange}
                    />
                    <div className={classes.buttonContainer}>
                        <Button variant="contained" color="primary" onClick={onCheckClick} className={classes.button}>
                            Check
                        </Button>
                    </div>

                    <Typography className={classes.text}>
                        After pressing the Check button the results of the evaluation will be displayed below. The
                        computation time may vary between 10 to 30 seconds.
                    </Typography>
                </Card>
                <div>
                    {evaluating && <CircularProgress size="150px"/>}
                </div>
                <Card className={classes.card}>
                    <Typography className={classes.text}>
                        The results of the evaluation will be displayed in this box. For each different URL identified, one or
                        more suspicious text chunks will be displayed. Inspection of the URLs is recommended for a
                        potential case of cross-language plagiarism.
                    </Typography>
                    <Typography className={classes.typography}>
                        {results}
                    </Typography>
                </Card>
            </Grid>
        </>
    );
};
export default Detection;