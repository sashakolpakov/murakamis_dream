# Complex cotangent parameters: a valid left-half lemma and a right-end obstruction

Research proof, 4 November 2026. The global cotangent root theorem
does not imply that its selected horizontal line dominates the
complete finite contour. The obstruction below is to that proposed
phase estimate, not to a finite-sum asymptotic or to the smaller
quadratic-taper parameter domain.

## 1. Left-half derivative geometry at negative height

Let \(P=p+i\alpha,\ Q=q+i\beta\), where
\[
 p,q>0,\qquad |\alpha|,|\beta|<1/2,
 \tag{1}
\]
and use the original inverse cotangents \(a,b\) and selected root \(s_*\)
from the [global cotangent theorem](research_mixed_global_cotangent_roots.md).
Suppose \(y=\Im s_*<0\). On the left horizontal half-period put
\(S(x)=\cot\pi(x+iy)\). This circle has the parametrization
\[
 S=r\sin\theta+i(v_0+r\cos\theta),\qquad
 v_0=\coth(-2\pi y)>1,\quad r=\operatorname{csch}(-2\pi y)>0,
 \quad 0\le\theta\le\pi.
 \tag{2}
\]
The angle \(\theta\) increases strictly with \(x\in[0,1/2]\).
In particular \(r^2=v_0^2-1\).

The original exponential derivative has the exact expression
\[
 \exp Q_{\epsilon,s}
 =\frac{(S+P)(S+Q)(S+i)^\epsilon}
              {(2i)^\epsilon(P-i)(Q+i)},\qquad \epsilon=0,1 .
 \tag{3}
\]
Therefore \(f(\theta):=\Re Q_{\epsilon,s}(x(\theta)+iy)\) is the sum
of \(\log|S+P|,\log|S+Q|\), and \(\epsilon\log|S+i|\), minus a
constant. The phase is regular throughout this left half: all
shifted real arguments lie strictly between zero and one, except
the unshifted endpoints which are nonreal here.

For a shift \(p+i\alpha\), set \(B=v_0+\alpha>0\). Then
\[
 |S+P|^2=p^2+B^2+r^2+2r(p\sin\theta+B\cos\theta).
 \tag{4}
\]
On \(0\le\theta\le\pi/2\), this positive expression has strictly
negative second derivative; hence its logarithm is strictly concave.
On \(\pi/2\le\theta\le\pi\), its first derivative is negative in
the interior. The same facts with non-strict intermediate inequalities
hold for \(S+i\), where \(p=0,B=v_0+1\). The two original factors
make the total strict.

**Lemma 1.** The function \(f\) is strictly concave on the first
angular quarter and strictly decreasing on the second. At the
selected root, \(0<\Im S_*<1<v_0\), so \(\theta_*>\pi/2\).
It is the unique downward zero of \(f\); before it there is at most
one upward zero. Consequently the selected root is the only interior
horizontal maximum on \([0,1/2]\), and
\[
 \max_{0\le x\le1/2}\Re Q_\epsilon(x+iy)
 =\max\{\Re Q_\epsilon(iy),\Re Q_\epsilon(s_*)\}.
 \tag{5}
\]
The right endpoint \(x=1/2\) is strictly below the selected maximum.

Indeed \(f(\pi/2)>f(\theta_*)=0\), while \(f\) decreases strictly
after \(\pi/2\). Strict concavity before \(\pi/2\) allows only
an initial negative segment followed by a positive one, or positivity
throughout. Integrating the resulting sign pattern of the actual
real derivative proves (5). This argument does not compare the
initial endpoint with the saddle, and says nothing about the right
horizontal half-period.

## 2. The original full-period phase, including upper shifted factors

Use the calibrated whole-half-plane factorial phases
\[
 g_-(z)=\frac{\operatorname{Li}_2(e^{-2\pi iz})-\pi^2/6}{2\pi i}
             \quad(\Im z<0),\qquad
 g_+(z)=\overline{g_-(\overline z)}+i\pi(z-z^2)
             \quad(\Im z>0).
 \tag{6}
\]
These come from the actual marked interpolation, by the
[lower-half theorem](research_lower_half_factorial_continuation.md)
and the [upper reflection calibration](research_mixed_all_real_conditional_packet.md).
In particular
\[
                  g_-(z+1)=g_-(z),\qquad
                  g_+(z+1)=g_+(z)-2\pi iz .
 \tag{7}
\]
On the original regular strip they agree with the original branches.
For a horizontal line on which every shifted imaginary part is
nonzero, define \(\mathcal Q_\epsilon\) using the appropriate
\(g_-\) or \(g_+\) separately for each of \(s,s+a,s+b\), with the
original chirp \(2\pi ias\). This is the leading phase of the actual
interpolated row on the whole line, including its shifted walls.
It is not obtained by making an upper shifted factorial periodic.

If
\[
       y<0,\qquad y+\Im a<0,\qquad y+\Im b>0,
 \tag{8}
\]
only the \(b\)-shifted factor uses the upper branch. Thus (7) gives
the exact real increment
\[
 \Re\mathcal Q_\epsilon(1+iy)-\Re\mathcal Q_\epsilon(iy)
              =2\pi(y+\Im b-\Im a).
 \tag{9}
\]
Unlike the real-neighbor situation, this may be large and positive.

## 3. A rational cotangent counterexample

Take type three, \(\epsilon=0\), and the exact rational values
\[
                  P=\frac1{10}+\frac7{20}i,\qquad
                  Q=\frac1{10}-\frac9{20}i.
 \tag{10}
\]
They lie strictly in (1). Its selected quadratic root is
\[
 S_*=\frac{-(P+Q)+
       \sqrt{(P+Q)^2+4-4i(Q-P)}}2,\qquad
 s_*=\frac1{2\pi i}\Log\frac{S_*+i}{S_*-i},
 \tag{11}
\]
where the square root has positive real part. The outward checker
places \(S_*\) in the global selected strip and verifies the original
zero logarithmic lift. Informational values are
\[
 \begin{split}
 a&\simeq .4639373415-.1148982591i,\\
 b&\simeq .4604165758+.1520743697i,\\
 s_*&\simeq .3910966220-.0110304486i.
 \end{split}
 \tag{12}
\]
Both shifted factors at the selected root stay in their original
regular real strip. The signs (8) hold. Direct outward evaluation
of disk dilogarithms in (6), with no upper branch substitution,
proves
\[
 \frac{22}{25}<\Re\mathcal Q_0(s_*)<\frac9{10},\qquad
 \frac{157}{100}<\Re\mathcal Q_0(1+i\Im s_*)<\frac{159}{100},
 \tag{13}
\]
and, more sharply,
\[
 \Re\mathcal Q_0(1+i\Im s_*)-\Re\mathcal Q_0(s_*)>\frac23 .
 \tag{14}
\]
It independently checks (9) and the positive selected horizontal
curvature. The diagnostic difference is approximately .68837125;
only the strict outward inequalities enter the result.

This also has a literal finite-interpolation interpretation. Let
\[
 T_N(s)=e^{2\pi iNa s}
   \frac{P_N(N(s+a))P_N(N(s+b))}{P_N(Ns)^2}.
 \tag{15}
\]
The two evaluation points \(s_*\) and \(1+i\Im s_*\), and all their
shifted arguments, lie in fixed open upper or lower half-planes.
Their original factorial expansions therefore have nonzero symbols
and give
\[
 \frac1N\log\frac{|T_N(1+i\Im s_*)|}{|T_N(s_*)|}
 \longrightarrow
 \Re\mathcal Q_0(1+i\Im s_*)-\Re\mathcal Q_0(s_*)>\frac23 .
 \tag{16}
\]
The same limiting rate holds at the actual right midpoint
\(1-1/(2N)+i\Im s_*\), by uniformity on a small nonreal compact.
Thus an upper bound putting the entire selected horizontal line
below its selected saddle is false on the full cotangent domain.

## 4. Scope

The root theorem, its zero lift and local coercivity remain valid
at (10). Lemma 1 remains valid as well. Equation (14) rules out
one proposed whole-horizontal estimate; it does not establish
which currents cancel after integration or which term leads the
complete canonical finite sum. No failure of a finite-sum
asymptotic or of a geometric outer contribution is proved.

The parameters (12) lie outside the smaller original quadratic-taper
height ranges. This obstruction does not decide horizontal
dominance or a full-source theorem on those taper ranges. Such a
theorem requires its own endpoint, shifted-factor and alias analysis.

## 5. Reproduction

    python3 experiments/check_mixed_complex_horizontal_obstruction.py --precision 256

The symbolic checks verify the cotangent derivative, circle formulas
and original upper-period increment. Outward complex arithmetic
certifies the explicit radical root, original lift, branch signs
and strict phase inequalities. No sampled maximum or floating
optimizer is used in acceptance.
