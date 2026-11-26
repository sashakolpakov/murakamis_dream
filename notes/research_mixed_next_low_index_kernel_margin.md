# A positive low-index kernel bound below the next geometric action

Research deduction, 7 November 2026. For a small physical incoming
index, the next conditional kernel admits a positive bound whose
exponential cost approaches an explicit constant. These constants,
added to the action of the adjacent three-crossing pendant, lie
strictly below the actual next action, for both next letters.

The smaller reserve occurs for an ordinary next three. We retain
a term of the original action that was dropped in the earlier
coarse bound. The proof below supplies the kernel and action
comparison. A bound for the incoming coefficient is a separate
input, stated precisely in Section 4. No numerical evaluation or
certificate replay is used.

## 1. Exact physical support and the positive bound

Put
\[
 r=e^{-2\pi i/N},\quad P_j=(r;r)_j,\quad S_j=|P_j|,\quad
 p_j(Z)=(rZ;r)_j,\quad
 J(t)=\int_0^t\log(2\sin\pi u)\,du .
 \tag{1}
\]
For \(\beta=0,1\), retain the entire conditional kernel
\[
 C_{\beta,N}(Y,Z)
    =\sum_{j=0}^{N-1}
           \frac{Y^{-j}p_j(Y)p_j(Z)}{P_j^{2+\beta}} .
 \tag{2}
\]
At a physical \(Y=r^b\), its original support gives
\[
 \frac{|p_j(r^b)|}{S_j}
   =\frac{S_{b+j}}{S_bS_j}\le\frac{2^b}{S_b}
                 \quad(j+b<N),\qquad
 p_j(r^b)=0\quad(j+b\ge N).
 \tag{3}
\]
The inequality follows by bounding each of the \(b\) factors
in \(S_{b+j}/S_j\) by two. The incoming chirp has modulus one.
Consequently
\[
 |C_{\beta,N}(r^b,Z)|
       \le \frac{2^b}{S_b}
             \sum_{j=0}^{N-1}\frac{|p_j(Z)|}{S_j^{1+\beta}} .
 \tag{4}
\]
We use the support only before taking this positive majorant.
No such termination is imposed at a nonphysical incoming value.

For \(0<\delta<1/6\), define
\[
             \omega(\delta)=\delta\log2-J(\delta).
 \tag{5}
\]
The uniform sine-factorial estimate, including both endpoints,
gives \(2^b/S_b\le CN^A e^{N\omega(\delta)}\) when
\(0\le b\le\delta N\). Here \(J\) is decreasing on
\([0,\delta]\), and \(\omega(\delta)\to0\) as
\(\delta\downarrow0\).

Write
\[
 L(u)=-2J((1-u)/2),\qquad
 M_\beta(C)=\max_{0\le u\le1}
                  \{L(u)-(1+\beta)J(u)+Cu\}.
 \tag{6}
\]
The [complete numerator estimate](research_mixed_boundary_strip_bounds.md),
Section 2, yields, on every fixed output disk \(|Z|\le R\),
\[
 \sum_{j=0}^{N-1}\frac{|p_j(Z)|}{S_j^{1+\beta}}
   \le C_\tau N^{A_\tau}
         e^{N\{M_\beta(\log_+R)+\tau\}}
                         \qquad(\tau>0).
 \tag{7}
\]
This includes every original row, numerator zero, and level parity.

## 2. The two required constants

The actual next-three ordinary output has imaginary part at most
\(17/250\), and its terminal private output has imaginary part
less than \(37/1000\). Both are covered by
\[
              \log_+|Z|\le C_*:=17\pi/125.
 \tag{8}
\]
For a next four both outputs have strictly negative imaginary
part, so \(|Z|<1\).

**Lemma 1.** The constants in (6) satisfy
\[
             M_0(C_*)<\frac{1271}{2500},
             \qquad M_1(0)<\frac7{15}.
 \tag{9}
\]

*Proof.* The second inequality is the already proved scalar bound
used in [the transformed initial interval](research_mixed_transformed_real_initial_interval.md),
equations (14)--(15). We prove the sharper first inequality here.

Put \(F(u)=L(u)-J(u)+C_*u\). On \(0<u<1\),
\[
 F'(u)=C_*-\log(2\sin(\pi u/2)),\qquad
 F''(u)=-(\pi/2)\cot(\pi u/2)<0.
 \tag{10}
\]
Its unique maximum lies between \(1/2\) and \(3/5\).
Indeed \(C_*>51/125>(\log2)/2\), since \(\log2<7/10\).
At \(u=3/5\), \(2\sin(3\pi/10)=(1+\sqrt5)/2>8/5\).
Also \(C_*<374/875<9/20<\log(8/5)\). For the last bound,
the exponential series gives
\[
 e^x\le1+x+\frac{x^2}{2(1-x/3)}\quad(0<x<3),
 \qquad
 1+\frac9{20}
       +\frac{(9/20)^2}{2(1-3/20)}<\frac85 .
 \tag{11}
\]
The estimate \(\log2<7/10\) follows by retaining four positive
terms of the exponential series at \(7/10\).

Throughout the maximizing interval,
\[
 -F''(u)\ge\frac\pi2\cot(3\pi/10)>
       \frac{25}{16}\frac57=\frac{125}{112}>\frac{11}{10}.
 \tag{12}
\]
Here \(\pi>25/8\), and
\(\cot(3\pi/10)=\tan(\pi/5)=\sqrt{5-2\sqrt5}>5/7\).
The last radical comparison follows, for example, from
\(\sqrt5<110/49\).

Let \(G\) be Catalan's constant and \(b_2=2G/\pi\).
The original sine integral gives
\[
                 F(1/2)=b_2/2+C_*/2.
 \tag{13}
\]
The bound \(G<229/250\) is established by the alternating
series in [the preparation-error proof](research_three_crossing_global_preparation_error.md),
Section 4. Together with \(\pi>333/106\), it implies
\[
             b_2<\frac{24274}{41625}<\frac7{12}.
 \tag{14}
\]
For an elementary rational witness for the bound on \(\pi\),
Machin's formula and the alternating arctangent series give
\[
 \pi>
 16\left(\frac15-\frac1{3\cdot5^3}
          +\frac1{5\cdot5^5}-\frac1{7\cdot5^7}\right)
                    -\frac4{239}>\frac{333}{106}.
 \tag{15}
\]
No new numerical approximation is involved.

The logarithm series at \(1/3\) gives
\[
 \log2=2\sum_{k\ge0}\frac{3^{-2k-1}}{2k+1}
       >\frac{842}{1215}>\frac{693}{1000}.
 \tag{16}
\]
Using \(\pi<22/7\), equations (13)--(16) yield
\[
 F(1/2)<\frac7{24}+\frac{187}{875},\qquad
 0<F'(1/2)<\frac{374}{875}-\frac{693}{2000}
                         =\frac{1133}{14000}.
 \tag{17}
\]
Integrating the curvature bound (12) and completing the square
therefore gives
\[
 M_0(C_*)<
       \frac7{24}+\frac{187}{875}
        +\frac5{11}\left(\frac{1133}{14000}\right)^2
                         <\frac{1271}{2500}.
 \tag{18}
\]
The last comparison is rational. After subtracting the first
two terms it is
\[
             \frac{1283689}{431200000}
                         <\frac{317}{105000},
 \tag{19}
\]
whose positive cross-product difference is \(1903055000\).
This proves the lemma. \(\square\)

Combining (4)--(9), define \(m_0=1271/2500\) and
\(m_1=7/15\). On the respective actual output families,
\[
 |C_{\beta,N}(r^b,Z)|
    \le C_\tau N^{A_\tau}
       e^{N\{m_\beta+\omega(\delta)+\tau\}},
                    \qquad 0\le b\le\delta N .
 \tag{20}
\]
The strict constants in (9) allow small fixed output neighborhoods.
Fixed output derivatives have polynomial cost, by applying Cauchy's
formula to each numerator polynomial before the positive sum.

## 3. Retain the previously omitted part of the actual action

Use \(y=t_2,s=s_3,z=t_3\) and the matched ordinary or terminal
references of [the local next-source theorem](research_mixed_three_four_next_local_source.md).
The exact action increment is
\[
 \mathcal P_\beta^+-\mathcal P_{34}
       =W(y,s)+W(s,z)-g(y)-\beta g(s)-2\pi isz .
 \tag{21}
\]
The [earlier typed lower bounds](research_mixed_three_four_next_binomial_end_bound.md),
Section 5, dropped the positive real terms
\(-\Re g(y)-\beta\Re g(s)\). They can be restored without
changing any primitive or normalization.

Set
\[
                         \chi=\frac{117}{800\pi}.
 \tag{22}
\]
The [reciprocal-factorial lower bound](research_mixed_fourier_weight_continuation.md),
equation (27), gives \(-\Re g(v)>\chi\) on the negative-height
part of its rectangle
\([.236,.364]+i[-.116,.012]\).
The actual \(y\in O_4\) is in this part. For a next four,
the actual \(s\in O_4\) or \(A_4\) is in it as well.
The actual domain inclusions are those in
[the last-row reference domains](research_mixed_actual_last_row_reference_domains.md).
Thus the same typed calculation now gives
\[
 \begin{array}{c|c}
 \text{next reference}&\Re\mathcal P_\beta^+(-2,z)\\ \hline
 \text{ordinary three}&>2+\chi\\
 \text{terminal three}&>52/25+\chi\\
 \text{ordinary four}&>199/100+2\chi\\
 \text{terminal four}&>41/20+2\chi .
 \end{array}
 \tag{23}
\]
In particular the next-four values exceed \(207/100\).

The recorded pendant action enclosure in
[action calibration, Section 6](research_three_crossing_action_volume_calibration.md)
gives \(M_{\mathrm{pend}}<769/500\).
Since \(\chi>819/17600\), the constants in (9) have the
strict comparison
\[
 \begin{split}
 (2+\chi)-(769/500+m_0)
   &>\frac{819}{17600}-\frac{29}{625}
                    =\frac{59}{440000},\\
 \frac{207}{100}-(769/500+m_1)
   &=\frac{49}{750}.
 \end{split}
 \tag{24}
\]
These comparisons concern the original conditional action and
the actual output domains. No new critical point or scalar
minimum was evaluated.

## 4. The incoming coefficient estimate that would finish the low band

Let \(\ell_{b,N}(w)\) denote the \(b\)-th Newton coefficient
of the complete ordinary \(33\) polynomial:
\[
 \ell_{b,N}(w)=(v(w)^TA_3^2)_b.
 \tag{25}
\]
The exact lowered-word identity writes the full next sum as
\[
 \mathcal F_{\beta,N}(w,Z)
   =\frac1{\kappa^2N}
        \sum_{b=0}^{D}(-q)^b
                    \ell_{b,N}(w)C_{\beta,N}(r^b,Z).
 \tag{26}
\]
It would therefore suffice to prove, for all sufficiently small
fixed \(\delta>0\),
\[
 \sup_{0\le b\le\delta N}|\ell_{b,N}(w)|
   \le C_\tau N^{A_\tau}
       e^{N\{M_{\mathrm{pend}}+\epsilon(\delta)+\tau\}},
             \qquad \epsilon(\delta)\longrightarrow0 .
 \tag{27}
\]
Here the color bound must be uniform in the real ordinary color
or on the fixed complex neighborhoods being claimed. A single
nodal asymptotic at \(b=0\) is insufficient.

If (27) holds, choose a fixed \(\delta>0\) so that
\(\epsilon(\delta)+\omega(\delta)\), followed by the common
finite-rate and parameter tolerances, consumes less than half
the smaller reserve in (24). Equations (20) and (26) then
bound the positive sum over \(b\le\delta N\) exponentially
below the next action. The number of terms and the factor
\(1/N\) change only polynomial prefactors.

Thus (27) is now a sufficient incoming estimate for both next
types, with a strictly positive, explicitly proved margin.
This note proves (20), (23), and (24); it does not assume
(27), declare the low band removed, or estimate the remaining
middle indices.
