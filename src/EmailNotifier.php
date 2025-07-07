<?php
namespace App;

class EmailNotifier implements NotifierInterface {
    public function send(Task $task): void {
        echo "Email sent for task: {$task->title}\n";
    }
}
