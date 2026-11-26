# A stronger calibrated closing-action floor

Private written deduction, 10 November 2026. The original complete
symmetric closing action satisfies
\[
                         M_g>\frac{163}{50}.
 \tag{1}
\]
The proof improves the real first-variation debit and retains the
already proved complete vertical debit. It does not pay the remaining
critical endpoint sector or assert a complete closing asymptotic.

No mathematical numerical evaluation, saved-value arithmetic, import,
compilation, or frozen-source edit is used.

## 1. The selected cubic along the real outgoing interval

Use the original calibrated phase and cubic of
[the taller-strip theorem](research_mixed_symmetric_closing_strip_phase_and_tail.md):
\[
 S'(u)=-\pi^{-1}\operatorname{arsinh}\{c(u)\tan(u/2)\},\qquad
 c=p+iq,\quad v=2c,\quad
 v^3-2iv^2-3v+2i-2\cos(u/2)=0.
 \tag{2}
\]
For real $0\le x\le\pi/2$, the original branch has
\[
                         p>3/4,\qquad1/4<q<1/3.
 \tag{3}
\]
Indeed the source gives $1/3<\Im v<2/3$. At $\Im v=1/2$
the imaginary cubic is $-\Re(v)^2/2+7/8<0$, whereas its
actual right side is zero; its derivative in that imaginary
coordinate is positive on the stated interval. This proves
the lower bound for $q$ in (3).

The complete-root inequality from
[the exact real-cut obstruction, (5)--(9)](research_mixed_next_first_quarter_real_cut_obstruction.md)
is $q(0)>29/100$. The real cubic at $x=0$ is
\[
                  1=p(4p^2-12q^2+8q-3).
 \tag{4}
\]
The quadratic $-12q^2+8q-3$ increases for $q<1/3$. If
$p(0)\ge17/20$, the right side of (4) would exceed
\[
 \frac{17}{20}
 \left(\frac{289}{100}-\frac{4223}{2500}\right)
                   =\frac{25517}{25000}>1.
\]
Thus $p(0)<17/20$.

Set $\Delta=3v^2-4iv-3$. On the real segment (3),
$\Re\Delta>0$, directly from $\Re v>3/2$ and
$1/2<\Im v<2/3$. Differentiating the original cubic gives
\[
                 c'(x)=-\frac{\sin(x/2)}{2\Delta}.
\]
Consequently $p$ decreases, so the uniform bound is
\[
                            p(x)<17/20.
 \tag{5}
\]
There is no new algebraic root or logarithmic lift in this argument.

## 2. A cubic improvement to the real return estimate

For any fixed $x$ in the segment, (3)--(5) give
\[
 \arg c<\arctan(4/9)<\pi/6,\qquad |c|^2<8/9.
 \tag{6}
\]
Writing the real equation in (2) as
\[
          4\Re(c^3)=\cos(x/2)-p(8q-3)
\]
also gives
\[
             \Re(c^3)>\frac14\left(\frac7{10}+\frac14\right)
                          =\frac{19}{80},
 \tag{7}
\]
because $\cos(x/2)\ge1/\sqrt2>7/10$ and $q<1/3$.

Let $F(r)=\Re\operatorname{arsinh}(cr)$, $0\le r\le1$,
on the original principal branch. The denominator argument
in the following expression lies between zero and twice
$\arg c$. Therefore
\[
 \begin{split}
 \Re\frac{c^3}{(1+r^2c^2)^{3/2}}
 &\ge\frac{\Re(c^3)}{|1+r^2c^2|^{3/2}}\\
 &>\frac{19}{80}\frac{45}{119}
   =\frac{171}{1904}>\frac1{12}.
 \end{split}
 \tag{8}
\]
For the first inequality, the argument of the quotient is
between zero and $3\arg c<\pi/2$, and is no larger than
the argument of $c^3$. For the second, (6) gives
$|1+r^2c^2|<17/9$, and
$\sqrt{17/9}<7/5$, hence its power $3/2$ is below $119/45$.
The last comparison is $2052>1904$.

Since $F''(r)=-r\Re[c^3/(1+r^2c^2)^{3/2}]$, two integrations
with $F(0)=0,F'(0)=p$ prove
\[
                    \Re\operatorname{arsinh}(cr)
                            \le pr-\frac{r^3}{72}.
 \tag{9}
\]
Substitute $r=\tan(x/2)\in[0,1]$ in (2). The real action
debit from zero to $\pi/2$ is bounded by
\[
 D_{\rm real}
 \le\frac1\pi\left\{\frac{17}{20}\log2
                                  -\frac{1-\log2}{72}\right\}.
 \tag{10}
\]
Here the two exact integrals are
$\int_0^{\pi/2}\tan(x/2)\,dx=\log2$ and
$\int_0^{\pi/2}\tan^3(x/2)\,dx=1-\log2$.

## 3. Written rational budget and original closing normalization

The positive atanh series gives the strict bound
\[
 \log2=2\operatorname{atanh}(1/3)
 <\frac23+\frac2{81}+\frac1{540}
 =\frac{1123}{1620}.
 \tag{11}
\]
In the tail beginning with the fifth power, replace every
denominator by $5$ and sum the geometric series; all subsequent
replacements are strict. The usual written Machin estimate is
\[
 \pi=16\arctan(1/5)-4\arctan(1/239)
 >16(1/5-1/375)-4/239>157/50.
 \tag{12}
\]
We also retain $\pi<22/7$. These are elementary series inequalities,
not evaluations of a geometric root or action.

The positive term in (10), the retained complete vertical debit,
and the cubic gain satisfy respectively
\[
 \begin{split}
 \frac{17\log2}{20\pi}
   &<\frac{19091}{101736}<\frac{751}{4000},\\
 D_{\rm vert}\le\frac2{27\pi}
   &<\frac{100}{4239}<\frac{59}{2500},\\
 \frac{1-\log2}{72\pi}
   &>\frac{3479}{2566080}>\frac{27}{20000}.
 \end{split}
 \tag{13}
\]
The final rational comparisons, with positive denominators, are
\[
 76364000<76403736,\qquad250000<250101,\qquad
                         69580000>69284160.
\]
The vertical debit in (13) is exactly the original bound in
[the taller-strip action proof, (15)--(17)](research_mixed_symmetric_closing_strip_phase_and_tail.md),
valid up to height $7/10$. In particular it applies at the actual
$K_g<7/10$.

Combining (10)--(13), the total debit is strictly less than
\[
 \frac{751}{4000}+\frac{59}{2500}-\frac{27}{20000}
                  =\frac{3755+472-27}{20000}=\frac{21}{100}.
 \tag{14}
\]
The calibrated complete source has
[the proved bound $M_3>46/25$](research_inner_three_complete_action_lower_bound.md).
Thus
\[
                \Re S(\pi/2-iK_g)>\frac{46}{25}-\frac{21}{100}
                                        =\frac{163}{100}.
 \tag{15}
\]
The actual original closing point is the maximum on this horizontal
by [the closing concavity theorem](research_mixed_symmetric_closing_horizontal_concavity.md).
At the endpoint $u=\pi/2-iK_g$, its original phase
$\Xi=2S+iu^2/\pi-iu$ has real part $2\Re S$. Equation (15)
therefore proves (1), with no additive constant or scalar changed.

On the wider right hyperbola, the critical endpoint sector has
the exact attached rate $2J(a_*,H_*)+K_g$, where
$J=\Re\psi(a_*-iH_*,0)-H_*/2+3a_*H_*/(2\pi)$.
Consequently the still-unproved bound
\[
                            J(a_*,H_*)<\frac{32}{25}
 \tag{16}
\]
would suffice for its payment, because
$2(32/25)+7/10=163/50$. This note proves the target action
floor, not (16), nor monotonicity of that critical endpoint value.

## 4. Frozen direct sources

| Source | SHA-256 |
|---|---|
| `research_mixed_symmetric_closing_strip_phase_and_tail.md` | `fa1224123389462fd7e29199f1045d0892c167225b4dd6f79ea5bd967a583795` |
| `research_mixed_next_first_quarter_real_cut_obstruction.md` | `d21bb5387258faadfdefd0f4bd2acfb5d002042c0e2e0de9c9e4448f0ef23c30` |
| `research_inner_three_complete_action_lower_bound.md` | `dd5153c7eabefe865b6fd1ed03e6f2fb08c63283f20fd48a999b625ec4836c42` |
| `research_mixed_symmetric_closing_horizontal_concavity.md` | `f7890776761cf7d59e015617b9daf89a240d0b57b1bd51c86ee1e03000782a0b` |

All four original source proofs and their needed phase, branch and
normalization statements were read. No frozen source is altered.
