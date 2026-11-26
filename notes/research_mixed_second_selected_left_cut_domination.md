# The left cut at a selected outgoing four-type coordinate

Research deduction and scalar-certificate design, 6 November 2026.
The analytic reduction below leaves exactly 128 fixed midpoint checks.
No check has been executed for this note. Its resulting uniform sign
remains conditional on those checks.

## 1. The original trial and its containing domain

Use the bare own-four phase from the
[second-selection reduction](research_mixed_second_selected_plateau_reduction.md):
\[
 Q(s;a,b)=g(s+a)+g(s+b)-3g(s)-g(a)-g(b)+2\pi ias,
 \qquad g'(w)=\Log(1-e^{-2\pi iw}).
 \tag{1}
\]
Put
\[
 \begin{split}
 l&=1/8,\qquad s_h=3/10+ih,\qquad
 a=x+ik,\quad b=y+iH,\quad H=1/100,\\
 x,y&\in P=[11/50,9/20],\qquad
 -39/500\le k\le21/1000,\qquad
 -51/500\le h\le-1/1000 .
 \end{split}
 \tag{2}
\]
The trial \(s_h\) belongs to the original main line
\([1/8,1/2]+ih\). Define
\[
 \Delta(x,y,k,h)=\Re\{Q(s_h;a,b)-Q(l;a,b)\},\qquad
 R_L=\Re Q(l;a,b),\quad
 R_0=\max_{1/8\le t\le1/2}\Re Q(t+ih;a,b).
 \tag{3}
\]
In particular \(R_0-R_L\ge\Delta\). The difference retains the
original chirp, and the two outer terms \(-g(a)-g(b)\) cancel.

## 2. Four corners and one incoming height suffice

For fixed \(k,h\), \(\Delta\) is separately strictly concave in
the two real targets. Indeed its two second derivatives are
\[
 \begin{split}
 \Delta_{xx}&=\pi\Re\{\cot\pi(s_h+a)-\cot\pi(l+a)\},\\
 \Delta_{yy}&=\pi\Re\{\cot\pi(s_h+b)-\cot\pi(l+b)\}.
 \end{split}
 \tag{4}
\]
Apply Lemma 1 of the
[four-type corner reduction](research_mixed_selected_four_left_row_corners.md)
with index real part \(3/10\). The index and both outer heights
in (2) have modulus at most \(.102\), exactly as required there.
Thus each derivative in (4) is strictly negative. Consequently
\[
 \Delta(x,y,k,h)\ge
 \min_{\xi,\eta\in\{11/50,9/20\}}\Delta(\xi,\eta,k,h).
 \tag{5}
\]

Let \(A(t,q)=\arg(1-e^{2\pi q-2\pi it})\) on the original strip.
The elementary radius bounds in the
[outgoing last-row proof](research_mixed_second_selected_outgoing_last_rows.md)
give
\[
 \pi\min(1-2t,0)\le A(t,q)\le\pi\max(1-2t,0).
 \tag{6}
\]
Differentiating the original difference, including the chirp, yields
\[
 \Delta_k=-A(3/10+x,h+k)+A(1/8+x,k)-7\pi/20.
 \tag{7}
\]
At \(x=11/50\), the two summed real parts are \(.52,.345\).
Equation (6) gives
\[
              \Delta_k\le .04\pi+.31\pi-.35\pi=0.
 \tag{8}
\]
At \(x=9/20\), the summed parts are \(.75,.575\). The second
argument in (7) is negative, and
\[
 -A(.75,h+k)=\arctan(e^{2\pi(h+k)})<\pi/3.
 \tag{9}
\]
For the last bound, \(h+k\le.020<.021\) and
\[
 e^{.042\pi}<e^{33/250}<\frac{250}{217}
                  <\frac{20}{17}<\sqrt3.
 \tag{10}
\]
Here \(\pi<22/7\), and \(e^q<1/(1-q)\) for \(0<q<1\)
follows directly from the positive series. The last two comparisons
are rational, including \((20/17)^2<3\). Therefore
\(\Delta_k<\pi/3-7\pi/20=-\pi/60\) at this second corner.
Both corner differences are nonincreasing in \(k\), uniformly in
the other real target and in \(h\). Define
\[
 d_{\xi,\eta}(h)=\Delta(\xi,\eta,21/1000,h).
 \tag{11}
\]
Equations (5), (8)--(9) prove
\[
 \Delta(x,y,k,h)\ge
               \min_{\xi,\eta\in\{11/50,9/20\}}d_{\xi,\eta}(h).
 \tag{12}
\]

## 3. A whole-interval bound from fixed midpoint values

Since the real cut is independent of \(h\),
\[
 \begin{split}
 d'_{\xi,\eta}(h)={}&-A(3/10+\xi,h+21/1000)
                   -A(3/10+\eta,h+1/100)\\
                 &+3A(3/10,h)-2\pi\xi .
 \end{split}
 \tag{13}
\]
The first three terms on the right are nonnegative. Hence
\(d'\ge-2\pi\xi\ge-9\pi/10\). Because \(h<0\), the sharper
radius bound \(A(3/10,h)\le\pi/5\) applies. Using (6) for the
other two arguments gives
\[
 d'\le\pi(2\xi-2/5)+\pi(2\eta-2/5)+3\pi/5-2\pi\xi
              =\pi(2\eta-1/5)\le7\pi/10.
 \tag{14}
\]
Thus \(9\pi/10\) is a Lipschitz constant for all four functions.

Partition \([-51/500,-1/1000]\) into 32 equal closed intervals.
For an interval \([l_j,r_j]\), let \(q_j=(l_j+r_j)/2\).
The following are 128 sufficient strict inequalities:
\[
 d_{\xi,\eta}(q_j)-\frac{9\pi}{10}\frac{r_j-l_j}{2}>\frac1{100},
 \qquad j=0,\ldots,31,\quad \xi,\eta\in\{11/50,9/20\}.
 \tag{15}
\]
They bound every height in each interval, including all endpoints.

The [standalone checker](../experiments/check_mixed_second_selected_left_cut_domination.py)
uses outward ball arithmetic at 160 bits and the original primitive
\[
              g(w)=\frac{\operatorname{Li}_2(e^{-2\pi iw})-\pi^2/6}
                                      {2\pi i}.
 \tag{16}
\]
It checks regular strips and separation from the dilogarithm cut.
It evaluates the canceled difference
\[
 \begin{split}
 \Delta={}&\Re\{g(s_h+a)-g(l+a)+g(s_h+b)-g(l+b)\\
            &\hspace{18mm}-3g(s_h)+3g(l)+2\pi ia(s_h-l)\}.
 \end{split}
 \tag{17}
\]
The exact height intervals, midpoint values, whole-interval rational
endpoints and all 128 signs are saved. The script checks its input
hashes before and after evaluation and refuses to overwrite a result.
There is no root, finite quantum sum, adaptive subdivision or earlier
certificate replay.

**Proposition 1 (certificate implication).** If all checks (15) pass,
then throughout (2)
\[
                         R_L<R_0-\frac1{100}.
 \tag{18}
\]
This follows from (12), the whole-interval Lipschitz bound and the
fact that \(s_h\) is an allowed main trial. Any common Fourier
allocation and original affine tangent preserve (18).

## 4. Exact finite consequence at the second selected position

Consider the actual position-2 setting with \(m\ge4\), first three
flags \((\alpha,1,\beta)\), position 1 unselected, and \(H_2=1/100\).
For \(\alpha=0\), the attached incoming height is in
\((-.072,.021)\), by the
[endpoint rectangle theorem](research_mixed_open_word_endpoint_rectangles.md).
For \(\alpha=1\), it is in \((-.078,-.020)\), by the
[coupled attached-height theorem](research_mixed_first_four_attached_height_bound.md).
The ordinary own-four index height is in \((-.102,-.001)\).
Thus all actual targets lie in (2), with no assumption that the
two input references lie in the older cyclic rectangles.

Retain \(\mathcal B_{23,N}\), \(\Lambda_{23}\), the bare profiles
\(R_i^2,R_j^3\), and the two rates \(W_2^\nu\) exactly as in
equations (4), (7), and (9)--(11) of the
[finite reduction](research_mixed_second_selected_plateau_reduction.md).
Put
\[
 \begin{split}
 D_{12}=\max_{\substack{i\in\{0,R\},\ j\in\{0,L,R\}\\
                       \nu\in\{\mathrm{fac},\mathrm{force}\}}}
 \{R_i^2+R_j^3-\tfrac\alpha2\Re g(z_1)
                   -\tfrac\beta2\Re g(z_3)+W_2^\nu-\Lambda_{23}\}.
 \end{split}
 \tag{19}
\]
Assume the 128 checks (15) pass, as well as the separate
[outgoing-selected four last-row checks](research_mixed_selected_outgoing_four_last_row_domination.md).
Then the complete finite-current bound is
\[
 \mathcal B_{23,N}\le C_\tau N^{A_\tau}
       \exp N\{\Lambda_{23}+\max(-1/400,D_{12})+\tau\},
                         \qquad \tau>0.
 \tag{20}
\]
Indeed the latter last-row comparison removes every left profile 1
by domination by profile 0. The
[right last-row theorem](research_mixed_second_selected_outgoing_last_rows.md)
pays all terms with right profile 1 and remaining left profile
\(0,L,R\) by \(1/400\). Equation (18) removes each remaining left
profile \(L\) by the corresponding profile 0. Exactly twelve terms,
those in (19), remain. These replacements preserve both complete
Fourier alternatives, both boundary halfweights and the original
two tangents; they do not partition a polynomial into artificial
branches.

Equation (20) retains the literal two finite kernels, all their rows
and currents, and both parities through the cited finite reduction.
The signs of the twelve remaining terms are not asserted. The
pointwise comparison (18) also includes incoming height \(1/100\),
but (20) is stated only for position 1 unselected; it does not supply
the separate cap comparison required for simultaneous selections.
