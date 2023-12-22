import {
  Select,
  SelectContent,
  SelectGroup,
  SelectItem,
  SelectTrigger,
} from "./ui/select";
import { GeneratedCodeConfig } from "../types";
import { Badge } from "./ui/badge";
import { Label } from "@radix-ui/react-label";

const myStyle = {
  color: 'blue', // You can set any color value here
  fontSize: '1.1rem', // 调整字体大小
  fontWeight: 'bold', // 设置为粗体
};
function generateDisplayComponent(config: GeneratedCodeConfig) {
  switch (config) {
    case GeneratedCodeConfig.HTML_TAILWIND:
      return (
        <div>
          <span className="font-semibold">HTML</span> +{" "}
          <span className="font-semibold">Tailwind</span>
        </div>
      );
    case GeneratedCodeConfig.REACT_TAILWIND:
      return (
        <div>
          <span className="font-semibold">React</span> +{" "}
          <span className="font-semibold">Tailwind</span>
        </div>
      );
    case GeneratedCodeConfig.BOOTSTRAP:
      return (
        <div>
          <span className="font-semibold">Bootstrap</span>
        </div>
      );
    case GeneratedCodeConfig.IONIC_TAILWIND:
      return (
        <div>
          <span className="font-semibold">Ionic</span> +{" "}
          <span className="font-semibold">Tailwind</span>
        </div>
      );
    case GeneratedCodeConfig.SVG:
      return (
        <div>
          <span className="font-semibold">SVG</span>
        </div>
      );
    default: {
      const exhaustiveCheck: never = config;
      throw new Error(`Unhandled case: ${exhaustiveCheck}`);
    }
  }
}

interface Props {
  generatedCodeConfig: GeneratedCodeConfig | undefined;
  setGeneratedCodeConfig: (config: GeneratedCodeConfig) => void;
  label?: string;
  shouldDisableUpdates?: boolean;
}

function OutputSettingsSection({
  generatedCodeConfig,
  setGeneratedCodeConfig,
  label = "生成主题",
  shouldDisableUpdates = false,
}: Props) {
  return (
    <div className="flex flex-col gap-y-2 justify-between text-sm">
      <div className="grid grid-cols-3 items-center gap-4">
        <span>{label}</span>
        <Select
          value={generatedCodeConfig}
          onValueChange={(value: string) =>
            setGeneratedCodeConfig(value as GeneratedCodeConfig)
          }
          disabled={shouldDisableUpdates}
        >
          <SelectTrigger className="col-span-2" id="output-settings-js">
            {generatedCodeConfig
              ? generateDisplayComponent(generatedCodeConfig)
              : "Select a stack"}
          </SelectTrigger>
          <SelectContent>
            <SelectGroup>
              <SelectItem value={GeneratedCodeConfig.HTML_TAILWIND}>
                {generateDisplayComponent(GeneratedCodeConfig.HTML_TAILWIND)}
              </SelectItem>
              <SelectItem value={GeneratedCodeConfig.REACT_TAILWIND}>
                {generateDisplayComponent(GeneratedCodeConfig.REACT_TAILWIND)}
              </SelectItem>
              <SelectItem value={GeneratedCodeConfig.BOOTSTRAP}>
                {generateDisplayComponent(GeneratedCodeConfig.BOOTSTRAP)}
              </SelectItem>
              <SelectItem value={GeneratedCodeConfig.IONIC_TAILWIND}>
                <div className="flex items-center">
                  {generateDisplayComponent(GeneratedCodeConfig.IONIC_TAILWIND)}
                  <Badge className="ml-2" variant="secondary">
                    Beta
                  </Badge>
                </div>
              </SelectItem>
              <SelectItem value={GeneratedCodeConfig.SVG}>
                <div className="flex items-center">
                  {generateDisplayComponent(GeneratedCodeConfig.SVG)}
                  <Badge className="ml-2" variant="secondary">
                    Beta
                  </Badge>
                </div>
              </SelectItem>
            </SelectGroup>
          </SelectContent>
        </Select>
      </div>
      {/* 底部链接部分 */}
      <div className="flex flex-col items-start mt-4"> {/* 添加 flex-col 使链接垂直堆叠 */}
        <Label className="font-light leading-relaxed" style={myStyle}>
          <a target="_blank" href="https://qm.qq.com/cgi-bin/qm/qr?k=gQtTFHCHgyXjsfcXgjKSPBPsNyCJrGDB&jump_from=webapi&authKey=1HpFhOgqS83goVf3Td009vpg09C31cCSRDQYvWeB7Gs5RpwVobiQDS0qAgEOtiq2">
            免费使用，加入QQ群:640541448
          </a><br></br><br></br>
        </Label>
        <Label className="font-light leading-relaxed" style={myStyle}>
          <a target="_blank" href="https://github.com/uuu555552/ptocode">
            源码地址，点个Star，免费体验
          </a>
        </Label>
      </div>
    </div>
  );
}

export default OutputSettingsSection;
