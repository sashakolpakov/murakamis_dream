# The complete selected source through the upper radial seam

Research deduction, 8 November 2026. Exact pairing of finite
numerator factors extends the complete seam estimate through the
entire segment \(Y=e^{2\pi h}\), \(0\le h\le1/100\).
It also gives a fixed neighborhood of that segment. Thus the
original selected contour has paid endpoint arcs at its prescribed
height, as well as paid vertical connections through the seam.
Both ordinary and terminal next-three and next-four outputs are
covered, with their original action normalizations.

The conclusion retains the whole prefix and the whole next
conditional kernel. It does not estimate the middle of the upper
horizontal complement or the lower horizontal complement.
No numerical evaluation or change to a frozen source is used.

## 1. Exact radial product bounds

Put \(D=N-1\), \(r=e^{-2\pi i/N}\), \(P_j=(r;r)_j\),
\(S_j=|P_j|\), and \(p_j(Y)=(rY;r)_j\). For \(R\ge1\), set
\[
 a_j(R)=\frac{|p_j(R)|}{S_j},\qquad
 b_j(R)=R^{-j/2}a_j(R),\qquad 0\le j\le D.
 \tag{1}
\]
The individual factors satisfy the exact identity
\[
 \frac{|1-Rr^k|^2}{|1-r^k|^2}
       =R+\frac{(R-1)^2}{|1-r^k|^2}.
 \tag{2}
\]
The factors of both products in (1) are at least one, and are
unchanged under \(k\mapsto N-k\). The full product is
\[
 A:=a_D(R)=\frac{R^N-1}{N(R-1)}
         =\frac1N\sum_{k=0}^{D}R^k\le R^D,\qquad
 B:=b_D(R)=R^{-D/2}A\le R^{D/2}.
 \tag{3}
\]
At \(R=1\) these formulas have their continuous value one.
They follow from the complete cyclotomic product, with
\(S_D=N\); no factorial denominator vanishes.

**Lemma 1.** For every level of either parity, every \(R\ge1\),
and every original row \(0\le j<N\),
\[
              a_j(R)\le R^D,\qquad
              R^{-j}a_j(R)\le R^{D/4}.
 \tag{4}
\]
For the first assertion use monotonicity of the positive prefix
products and (3). If \(2j\le D\), the first and last \(j\)
factors of \(B\) are disjoint and equal, so \(b_j^2\le B\).
Therefore
\[
 R^{-j}a_j=R^{-j/2}b_j
          \le R^{D/4-j/2}\le R^{D/4}.
\]
If \(2j\ge D\), use \(b_j\le B\):
\[
 R^{-j}a_j\le R^{(D-j)/2}\le R^{D/4}.
\]
These two cases include the middle row whether \(N\) is even or
odd. They prove the lemma.

Keep the exact polynomial \(d_N\). The identity
\[
       d_N(Y)=\frac1N\sum_{j=0}^{D}\frac{p_j(Y)}{P_j}
 \tag{5}
\]
is [the first-node theorem, Lemma 1](research_mixed_next_three_first_physical_node.md).
It is an entire identity, including the polynomial forcing.
Equations (3)--(5) give
\[
            |d_N(R)|R^{-N}\le R^{D-N}=R^{-1}\le1 .
 \tag{6}
\]
This bound uses the selected factor exactly once. It is not an
estimate for the unselected \(d_N(R)\) with that factor omitted.

## 2. The complete source on the radial segment

Use the literal original functions
\[
 \begin{split}
 U_{0,N}(w,X)&=\sum_{e=0}^{D}
                  H_N(w,r^{-e})p_e(X)/P_e,\\
 C_{\beta,N}(Y,Z)&=\sum_{j=0}^{D}
           Y^{-j}p_j(Y)p_j(Z)/P_j^{2+\beta},\\
 F_N(w,Y)&=F_{34,N}(w,Y)
          =N\operatorname{CT}_X[U_{0,N}(w,X)C_{1,N}(X,Y)],\\
 \mathscr D_{\beta,N}(w,Y,Z)
       &=F_N(w,Y)d_N(Y)Y^{-N}C_{\beta,N}(Y,Z).
 \end{split}
 \tag{7}
\]
Thus the selected Fourier contribution is
\(N[Y^N](F_Nd_NC_\beta)=
N\int_{\Gamma_1}\mathscr D_{\beta,N}(w,e^{-2\pi iy},Z)\,dy\)
on any increasing full period. Every source coefficient in (7)
is complete.

Write \(b_0=101/125\), \(c_{\rm b}=-2J(1/6)\), and
\[
 L(t)=-2J((1-t)/2),\qquad
 M_\beta(C)=\max_{0\le t\le1}
             \{L(t)-(1+\beta)J(t)+Ct\}.
 \tag{8}
\]
The full coherent coefficient norm and finite binomial estimate
in [the seam theorem, Section 3](research_mixed_next_complete_source_seam_collar.md)
give, uniformly on \(|X|=1\),
\[
 |U_{0,N}(w,X)|\le C_\tau N^B
                       e^{N(b_0+c_{\rm b}+\tau)}.
 \tag{9}
\]
They hold for all real ordinary colors and on sufficiently small
fixed complex complete-color disks. The same source supplies
\[
 c_{\rm b}<\frac{13}{40},\qquad
 \sup_{|X|\le1}\sum_{j<N}\frac{|p_j(X)|}{S_j^2}
                  \le C_\tau N^B e^{N(7/15+\tau)}.
 \tag{10}
\]
Its proof keeps each \(H_N\) coherent.

Let \(R=e^c\), \(0\le c\le\pi/50\). The first bound in (4)
and (10) show
\[
 \sup_{|X|=1}|C_{1,N}(X,R)|
       \le C_\tau N^B e^{N(7/15+c+\tau)}.
 \tag{11}
\]
Insert (9)--(11) in the complete \(X\)-circle integral in (7),
including its factor \(N\):
\[
 |F_N(w,R)|\le C_\tau N^B
              e^{N(b_0+c_{\rm b}+7/15+c+\tau)}.
 \tag{12}
\]
The second inequality in (4), with the original incoming
chirp \(R^{-j}\), gives for every fixed output disk \(|Z|\le T\)
\[
 |C_{\beta,N}(R,Z)|\le
 R^{D/4}\sum_{j<N}\frac{|p_j(Z)|}{S_j^{1+\beta}}
 \le C_\tau N^B
     e^{N\{M_\beta(\log_+T)+c/4+\tau\}}.
 \tag{13}
\]
The last inequality is the whole-index disk numerator estimate
in [the low-index kernel margin, equation (7)](research_mixed_next_low_index_kernel_margin.md).
No physical support restriction is imposed on \(Y=R\).

Combining (6), (12), and (13) proves the full selected-source bound
\[
 \boxed{\quad
 \sup_{|Z|\le T}|\mathscr D_{\beta,N}(w,R,Z)|
 \le C_\tau N^B
 e^{N\{b_0+c_{\rm b}+7/15+M_\beta(\log_+T)+5c/4+\tau\}} .
 \quad}
 \tag{14}
\]
In particular the total radial cost is at most \(\pi/40\).
Neither the forced polynomial part of \(d_N\) nor any upper
conditional row is discarded.

## 3. An exact finite neighborhood of the entire segment

Fix \(0<\varepsilon<1/2\) and suppose
\[
                  |Y-R|\le\varepsilon,\qquad
                         1\le R\le e^{\pi/50}.
 \tag{15}
\]
Equation (2) implies \(|1-Rr^k|\ge|1-r^k|\). Therefore
\[
 |p_j(Y)|\le |p_j(R)|
       \prod_{k=1}^{j}\left(1+\frac{\varepsilon}{|1-r^k|}\right)
       \le |p_j(R)|e^{N\Omega(\varepsilon)},
 \tag{16}
\]
where the exact all-level bound in Section 1 of the seam theorem is
\[
 \Omega(\varepsilon)=\log(1+\varepsilon/2)
          +\frac{\varepsilon}{2}\log(1+2/\varepsilon)
                 \longrightarrow0 .
 \tag{17}
\]
Also \(R/|Y|\le(1-\varepsilon)^{-1}\).
Apply (16) to the prefix, the exact sum (5), and the next kernel.
The two inverse powers, \(Y^{-N}\) and \(Y^{-j}\), cost at most
two factors \((1-\varepsilon)^{-N}\). Thus (14) holds throughout
the tube (15) with the additional rate
\[
                E(\varepsilon)=
          3\Omega(\varepsilon)-2\log(1-\varepsilon)
                      \longrightarrow0 .
 \tag{18}
\]
This is a finite algebraic estimate with a uniform neighborhood
of the prescribed segment. It does not extend a single nodal value
by an unspecified analytic-continuation argument.

## 4. Comparison with every actual next action

Use the original conditional action \(\mathcal P_\beta^+\) and
the matched ordinary and terminal next references from
[the local next-source theorem](research_mixed_three_four_next_local_source.md).
The output domains and scalar bounds in the seam theorem are
\[
 \begin{array}{c|c|c}
 \text{output}&T&M_\beta(\log_+T)\ \text{upper bound}\\ \hline
 \text{next four}&1&7/15\\
 \text{next three with }|Z_*|\le1&1&13/40\\
 \text{arbitrary typed next three}&e^{17\pi/125}&1271/2500 .
 \end{array}
 \tag{19}
\]
The negative-height or nonpositive-height restrictions are imposed
only at the actual reference; a small disk enlargement preserves
all strict bounds.

The stronger action bounds are proved in
[the next-four pair theorem](research_mixed_next_four_real_pair_action_floor.md)
and [the next-three pair theorem](research_mixed_next_three_real_pair_action_floor.md).
They give the following strictly smaller rational lower bounds.
The third column is a strictly larger rational ceiling for (14)
before \(\tau\), using \(5c/4\le\pi/40<11/140\):
\[
 \begin{array}{c|c|c}
 \text{actual reference}&\Re\mathcal P_\beta^+(-2,z_*)
                         \text{ lower bound}&
                    \text{selected-source ceiling}\\ \hline
 \text{ordinary four}&109/50&43/20\\
 \text{terminal four}&56/25&43/20\\
 \text{ordinary three, }h_z\le0&419/200&201/100\\
 \text{ordinary three, }h_z\ge0&441/200&219/100\\
 \text{terminal three}&89/40&219/100 .
 \end{array}
 \tag{20}
\]
For clarity, the three source comparisons in this table are
\[
 \frac{6199}{3000}+\frac{11}{140}<\frac{43}{20},\qquad
 \frac{2887}{1500}+\frac{11}{140}<\frac{201}{100},\qquad
 \frac{31621}{15000}+\frac{11}{140}<\frac{219}{100}.
 \tag{21}
\]
Their positive differences are \(107/21000\), \(71/10500\),
and \(353/105000\), respectively.
The smallest action-minus-ceiling difference in (20) is
\(3/200\). Both ordinary-three sign subfamilies have strict
reserves at \(h_z=0\). Compactness therefore supplies uniform
local neighborhoods without imposing a sign condition on nearby
complex parameter values.

**Theorem.** For some fixed \(\varepsilon>0\), the complete
selected density (7), on the whole tube (15), is exponentially
smaller than the original next action at every ordinary and
terminal next-three or next-four reference. The statement holds
for both parities and every real ordinary color, normalized
against the complete-color action. It also holds on fixed small
complex complete-color and actual-output neighborhoods.
Every fixed normalized mixed derivative has, on smaller
neighborhoods, the bound
\[
 \partial^\alpha
 \left[e^{-N\mathcal P_\beta^+(w,z)}
       \mathscr D_{\beta,N}(w,e^{-2\pi iy},e^{-2\pi iz})\right]
                         =O_\alpha(e^{-N/1000}).
 \tag{22}
\]

Choose \(E(\varepsilon)\), the total source tolerance, and the
parameter-neighborhood variation inside the strict reserve
\(3/200\). This proves a uniform value bound with a smaller
fixed loss. Markov's inequality for the complete polynomial in
the real ordinary color gives its fixed ordinary derivatives.
The original complex-color norms and Cauchy's formula prove
(22). Contours and neighborhoods are fixed before differentiating.
For \(\beta=1\), the output halfweight can be restored locally
using its actual nonzero factorial packet, with the exact action
shift \(-\Re g(z_*)/2\). This gives the original affine allocation
at the actual ordinary output, not an estimate at every independent
outgoing plateau coordinate.

## 5. The old filtered prefix and the actual top endpoint arcs

Let \(F_N^{\rm mid}=F_N-E_N^{\rm all}\) be the specific older
\(11/12\) filtering of
[paired localization, Section 5](research_mixed_next_low_cardinal_paired_localization.md).
Its complete correction has degree at most \(D\), and
\[
       \sup_{|Y|\le1}|E_N^{\rm all}(w,Y)|
                          \le CN^B e^{77N/50}.
 \tag{23}
\]
Consequently \(|E_N^{\rm all}(w,R)|\le
CN^B e^{77N/50}R^D\). Equations (6), (13) give the same
selected radial estimate as (14), with the prefix constant
\(b_0+c_{\rm b}+7/15\) replaced by \(77/50\).
For the tube use polynomial degree to add at most
\(\log(1+\varepsilon)\), and (16)--(18) for the other factors.
All extra costs tend to zero.
Since
\[
       \frac{77}{50}<b_0+\frac{13}{40}+\frac7{15}
                              =\frac{4799}{3000},
 \tag{24}
\]
the same conservative comparisons (20)--(21) apply to the
correction. Exact subtraction therefore proves the theorem for
\(F_N^{\rm mid}\) as well. This retains the specified old filter;
no \(77/50\) claim is made for the later \(8/9\) correction.

The exponential map takes \(y=ih\), \(0\le h\le1/100\), onto
the radial segment. A fixed sufficiently small angular width
\(\delta>0\) satisfies
\[
 e^{-2\pi i(x+ih)}\ \text{belongs to (15)}
 \quad\text{if}\quad
 \operatorname{dist}(x,\mathbb Z)\le\delta,\quad
                     0\le h\le1/100 .
 \tag{25}
\]
For example use
\(|e^{-2\pi ix}-1|\le2\pi|x|\) and boundedness of \(R\).
Hence the original upper cycle at height \(1/100\) has paid
endpoint arcs \([0,\delta]+i/100\) and
\([1-\delta,1]+i/100\). Vertical seam connectors over this
height range, and fixed paths in the same tube, are also paid.
Their original density is \(+N\,dy\); the inner factor \(N\)
in (7) and the next-row restoration
\(\kappa_N^{4+\beta}N^{1+\beta}P_k^{1-\beta}\) remain unchanged.

This is an estimate for the selected density. The cancellation
in (6) is not assigned to the unselected density. A paired
meromorphic kernel must still retain its actual denominator and
residues before applying these bounds.
The two remaining upper intervals between the endpoint arcs and
the central segment, and the nonlocal lower complement, remain
unestimated here. No full next-transfer or short-filling theorem
is asserted.
