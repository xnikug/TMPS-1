<?php
namespace App;

class EmailNotifier implements NotifierInterface {
    private string $smtpHost;
    private int $smtpPort;

    public function __construct(string $smtpHost = 'localhost', int $smtpPort = 587) {
        $this->smtpHost = $smtpHost;
        $this->smtpPort = $smtpPort;
    }

    public function send(Task $task): void {
        echo "Email sent via {$this->smtpHost}:{$this->smtpPort} for task: {$task->title}\n";
        echo "To: {$task->assignedTo}\n";
        echo "Subject: New Task Assigned - {$task->title}\n";
        echo "Body: {$task->description}\n";
        echo "---\n";
    }
}