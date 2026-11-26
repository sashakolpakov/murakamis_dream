# The first cap with the low rows and half-index rows of its neighbor

Research proof, 10 November 2026. At the original geometric
heights, the first cap and specified physical rows of the next ordinary
factor have a strict combined bound throughout the early interval.
The first cap is summed completely. The ordinary rows are those
below the previously proved left cut: \(3/20\) for an own-three
factor, and \(1/8\) for an own-four factor. The estimate also includes
the row at half the level, or the two adjacent rows when the level
is odd.

The proof transports their product from real coordinate \(11/50\).
It does not require a separate geometric upper bound for the cap
throughout the early interval. In particular, it retains the small
upper-row excess that can occur at a positive first height.
The remaining ordinary rows, the first coordinate's other Fourier
choice, and the original contour with changing heights are separate.

## 1. Exact finite quantity and original reference

Fix an actual positive three/four open word of length at least three.
Let the first two types be \(3+\alpha,3+\epsilon\), with
\(\alpha,\epsilon\in\{0,1\}\). Write their retained reference
coordinates as
\[
 a_*=a_0+ic,\qquad b_*=b_0+id,\qquad
 P=[11/50,9/20].
\tag{1}
\]
Here \(b_*=t_2^*\), and the second vertex is ordinary.
The first private reference is \(e_*\). The actual ranges are
those of the endpoint and ordinary source theorems:
\[
 -.108<c<.021,\qquad -.102<d<.068.
\tag{2}
\]
If \(\alpha=1\), then \(c<-.020\). If \(\epsilon=1\),
then \(d<0\). We retain the actual correlated reference rather
than allowing every independent point of these containing boxes.

For targets
\[
 a=x+ic,\quad b=z+id,\qquad
 1/10\le x\le11/50,\quad z\in P,
\tag{3}
\]
set \(r_N=e^{-2\pi i/N}\), \(P_j=(r_N;r_N)_j\),
\(p_j(X)=(r_NX;r_N)_j\), \(X=e^{-2\pi ia}\), and
\(Y=e^{-2\pi ib}\). The original ordinary rows are
\[
 R_{j,N}(a,b)=X^{-j}\frac{p_j(X)p_j(Y)}{P_j^{\,2+\epsilon}}.
\tag{4}
\]
Let \(U_{\alpha,N}(w,X)\) be the complete first-cap polynomial,
and \(d_N\) the original reciprocal-factorial interpolation
polynomial. Put
\[
 \ell_0=3/20,\quad\ell_1=1/8,\quad
 L_{\epsilon,N}=\lfloor N\ell_\epsilon\rfloor,\qquad
 H_N=\{\lfloor N/2\rfloor,\lceil N/2\rceil\}.
\tag{5}
\]
The quantity to estimate is
\[
 \mathcal B_N(w;x,z)=
 |U_{\alpha,N}(w,X)|\,|d_N(X)|^\alpha
 |d_N(Y)|^{\epsilon/2}
 \left\{\sum_{j=0}^{L_{\epsilon,N}}|R_{j,N}(a,b)|
                  +\sum_{j\in H_N}|R_{j,N}(a,b)|\right\}.
\tag{6}
\]
Every cap row and every ordinary row in the displayed range is
included. The set \(H_N\) has one element at even levels and two
at odd levels. These are unselected Fourier weights; no factor
\(1+X^{-N}\) is included in (6).

Use the original primitives \(J'(v)=\log(2\sin\pi v)\),
\(g(v)=J(v)+i\pi(v-v^2)/2\), with \(J(0)=0\) and the
continuation from positive real sine. The complete-end action is
\[
 S(e)=\operatorname{stat}_{u}
 \{-2J(1/2-u)-3J(u)-J(e-u)+i\pi eu\},
\]
where \(\operatorname{stat}\) means the value at the original
selected critical point. In particular
\(g'(v)=\log(1-e^{-2\pi iv})\) on its original lift. Set
\[
\begin{split}
 \Xi_\alpha(e,a)
 &=S(e)+J(e+a)-J(a)-i\pi ea-\alpha g(e)
                                      -\frac{\alpha}{2}g(a),\\
 F_{\alpha\epsilon}(s;a,b)
 &=g(s+a)+g(s+b)-(2+\epsilon)g(s)+2\pi ias\\
 &\hspace{9mm}-(1+\alpha/2)g(a)-(1+\epsilon/2)g(b).
\end{split}
\tag{7}
\]
The original critical actions are
\(L_\alpha(a)=\operatorname{stat}_e\Xi_\alpha(e,a)\) and
\(\phi_{\alpha\epsilon}(a,b)=\operatorname{stat}_s
F_{\alpha\epsilon}(s;a,b)\). They have these allocations,
and their first-coordinate marginals cancel:
\[
 L_\alpha'(a_*)+\partial_a\phi_{\alpha\epsilon}(a_*,b_*)=0.
\tag{8}
\]
Let \(\kappa_*=1/2500000\), and define
\[
\begin{split}
 \Gamma(z)={}&\Re L_\alpha(a_*)
   +\Re\phi_{\alpha\epsilon}(a_*,b_*)\\
 &+\Re\partial_b\phi_{\alpha\epsilon}(a_*,b_*)(z-b_0)
                              -\kappa_*(z-b_0)^2 .
\end{split}
\tag{9}
\]
The value and the remaining slope in (9) belong to the original
geometric solution. They are not chosen to fit the new estimate.

## 2. The combined derivative is positive

Keep \(s\in\{\ell_\epsilon,1/2\}\) real, and let
\[
 e\in E_c=[27/100,49/100]+i[-11/200,1/25].
\tag{10}
\]
This includes both real cap cuts, both horizontal aliases, and
the entire horizontal segment through its original private root.
Any alias penalty is independent of \(x\).

Set \(r=e^{2\pi c}\), \(R=e^{2\pi\Im e}\), and \(u=\Re e\).
The original height bounds give
\[
 1/2<r<23/20,\qquad R>2/3,\qquad
                    r<9/10\quad\hbox{if }\alpha=1.
\tag{11}
\]
These bounds follow from the elementary exponential estimates in
the early-cap proofs. Differentiating (7) without changing a
logarithmic lift gives
\[
 \partial_x\Re\{\Xi_\alpha(e,a)+F_{\alpha\epsilon}(s;a,b)\}
 =
 \log\frac{|1-rR e^{-2\pi i(u+x)}|
                 |1-r e^{-2\pi i(s+x)}|}
                {|1-r e^{-2\pi ix}|^{\,2+\alpha}} .
\tag{12}
\]
The ordinary chirp has real derivative zero because \(s\) is
real. The complete first Fourier weight accounts for the
exponent \(2+\alpha\) in the denominator.

**Lemma 1.** The derivative in (12) is strictly positive on
(3), (10). If \(\alpha=0\) and \(4/25\le x\le11/50\), it is
greater than \(18/125\).

*Proof.* Denote the squared moduli of the first numerator,
second numerator and denominator by \(A,C,B\), respectively.
It is enough to show \(AC>B^{2+\alpha}\).

For \(x\le4/25\), the angular bounds are
\[
 \cos(2\pi(u+x))<-1/2,\quad
 \cos(2\pi(s+x))<1/6,\quad
 \cos(2\pi x)>1/2.
\]
Consequently
\[
 A>1+\frac49r^2+\frac23r=:A_0,\quad
 C>1+r^2-\frac13r=:C_0,\quad
 B<1+r^2-r=:B_0.
\]
Direct multiplication gives
\[
 A_0C_0-B_0^2
 =\frac r{27}(63-48r+68r^2-15r^3)>0.
\tag{13}
\]
Indeed \(r<6/5\), so the parenthesis exceeds
\(63-48r+50r^2\), a positive quadratic with negative
discriminant. If \(\alpha=1\), then \(r<1\) and \(B_0<1\),
so \(A_0C_0>B_0^2>B_0^3\).

For \(4/25\le x\le11/50\), the angular bounds instead give
\[
 \cos(2\pi(u+x))<-6/25,\quad
 \cos(2\pi(s+x))<-9/50,\quad
 \cos(2\pi x)>9/50.
\]
Thus we may now use
\[
 A_0=1+\frac49r^2+\frac8{25}r,\quad
 C_0=1+r^2+\frac9{25}r,\quad
 B_0=1+r^2-\frac9{25}r.
\tag{14}
\]
For \(r<23/20\),
\[
 A_0-B_0=r\left(\frac{17}{25}-\frac59r\right)>0,
 \qquad C_0-B_0=\frac{18}{25}r.
\]
Furthermore \(r+r^{-1}\le5/2\) on \([1/2,23/20]\).
Hence
\[
 \frac{C_0}{B_0}>1+\frac{36}{107}=\frac{143}{107}.
\]
For \(\alpha=0\), (12) is therefore greater than
\[
 \frac12\log(143/107)>
 \frac{143-107}{143+107}=\frac{18}{125}.
\tag{15}
\]
The logarithm inequality follows by integrating
\(1/t\), or from its positive atanh series.

For \(\alpha=1\), put \(a=A_0-B_0\), \(c'=C_0-B_0\).
On \(1/2\le r\le9/10\),
\[
 2(a+c')-B_0=-1+\frac{79}{25}r-\frac{19}{9}r^2>0.
\tag{16}
\]
The quadratic is concave; its endpoint values are \(47/900\)
and \(67/500\). Also \(B_0\le743/500<3/2\). Thus
\[
 A_0C_0=(B_0+a)(B_0+c')
       >\frac32B_0^2>B_0^3.
\tag{17}
\]
This proves all assertions.

For clarity, the trigonometric bounds used above concern the
interval \(u+x\in[.37,.71]\). For the low cut,
\(s+x\in[.225,.37]\); for the half row,
\(s+x\in[.6,.72]\), with
\(\cos(2\pi(s+x))=-\cos(2\pi x)\).
The three nontrivial endpoint estimates
in the second case are
\(\sin(.08\pi)>6/25\), \(\sin(.07\pi)>1/5\), and
\(\sin(.06\pi)>9/50\); each follows from
\(\sin t\ge t-t^3/6\) and \(157/50<\pi<22/7\).
In the first case \(\cos(.45\pi)=\sin(.05\pi)<1/6\).
\(\square\)

## 3. The complete cap, including its upper physical rows

Use the [complete fixed-height early-cap theorem](research_mixed_cap_early_fixed_height_full_source.md).
At complete ordinary color its five
allocated profiles are the main line through \(\Im e_*\), the
two real cuts \(e=.27,.49\), and the two aliases at private
heights \(-.055,.04\), with penalties \(.11\pi,.08\pi\).
The true-end profile is
\[
 E_{\rm end}(c)-\frac{\alpha}{2}\Re g(a),\qquad
 E_{\rm end}(c)=\frac35+2\pi c_++\frac{\log4}{100}.
\tag{18}
\]
There is one additional allowance: the right-cut profile can
increase by less than \(1/200\) when \(\alpha=0,c>0,x<4/25\).
For \(x\ge4/25\), or \(c\le0\), this allowance is zero.
Every physical cap row, contour side and parity is included in
that source statement.

Lemma 1 applies to each of the five cap profiles after adding
\(\Re F_{\alpha\epsilon}(s;a,b)\), for either
\(s=\ell_\epsilon\) or \(s=1/2\).
It commutes with the maximum over the unchanged private
interval. Thus their combined rates do not exceed their values
at \(x=11/50\). The extra right-cut allowance is paid as well:
when it is present, transport just from \(4/25\) to \(11/50\)
saves more than
\[
 \left(\frac{11}{50}-\frac4{25}\right)\frac{18}{125}
                         =\frac{27}{3125}>\frac1{200}.
\tag{19}
\]
The remaining transport down to \(x\) is favorable.

The true-end profile requires a separate comparison. Its
combined derivative is
\[
 \log\frac{|1-r e^{-2\pi i(s+x)}|}
                {|1-r e^{-2\pi ix}|^{\,1+\alpha}} .
\tag{20}
\]
For \(s=\ell_\epsilon\), the numerator exceeds the single
denominator modulus because \(0<x<x+\ell_\epsilon<1/2\).
For \(s=1/2\), the same assertion follows from
\[
 |1+r e^{-2\pi ix}|^2-|1-r e^{-2\pi ix}|^2
                         =4r\cos(2\pi x)>0.
\]
For \(\alpha=0\), (20)
is positive. For \(\alpha=1\), it is greater than
\(-\log2\), because \(r<1\).
The latter transport can cost at most
\[
 \frac3{25}\log2<\frac{21}{250}.
\tag{21}
\]

At \(x=11/50\), the original bare cap plane exceeds \(79/100\),
by Section 6 of [the plateau phase proof](research_mixed_first_cap_plateau_phase.md).
For \(\alpha=0\),
\(E_{\rm end}(c)<3/4\). For \(\alpha=1\), \(c<0\) and
\(E_{\rm end}(c)<123/200\), leaving a reserve greater than
\(7/40\). Convexity of \(\Re g(x+ic)\) makes the allocated
cap-plane comparison at least as favorable as this bare
comparison. Since
\[
 \frac7{40}-\frac{21}{250}=\frac{91}{1000}>0,
\tag{22}
\]
the possible transport cost (21) is paid. Thus the true-end
profile also stays below the required joint plane.

At the comparison point \(x=11/50\), the original cap main
and four complementary profiles are bounded by its
[completed cap plane](research_mixed_first_cap_plateau_completion.md).
The complete ordinary row at \(\ell_\epsilon\) is below its
ordinary plane by \(1/2000\), for either own type. These
are the completed old-cut comparisons collected in
[ordinary-source assembly](research_mixed_three_row_source_assembly.md);
no claim about the
larger row \(1/5\) is used. The
[completed half-row comparison](research_mixed_half_row_support_completion.md)
gives exactly the same deficit and quadratic coefficient for
\(s=1/2\), on every required own/external type and in both
orientations. It uses the same correlated reference and
allocations as (7).
Adding the planes cancels their first-coordinate slopes by (8).
The two first-coordinate quadratic losses can be discarded.
Consequently every combined profile just considered is at most
\[
                         \Gamma(z)-1/2000 .
\tag{23}
\]

## 4. The finite-source bound

The [exact row-ratio lemma](research_mixed_first_attached_low_row_transport.md)
for the adjoining low tail holds for
every index \(0<u\le1/5\), on a height box containing (2).
The same finite geometric-series proof, stopped at (5), gives
\[
 \sum_{j=0}^{L_{\epsilon,N}}|R_{j,N}(a,b)|
                    <201\,|R_{L_{\epsilon,N},N}(a,b)|.
\tag{24}
\]
It does not require cancellation. The regular factorial
estimate gives the allocated rate
\(\Re F_{\alpha\epsilon}(\ell_\epsilon;a,b)\) for the last
row. Rounding (5) changes it by \(O(\log N/N)\).
Each row in \(H_N\) has the allocated rate
\(\Re F_{\alpha\epsilon}(1/2;a,b)+O(\log N/N)\).
These estimates are uniform: the half-row factorial arguments
remain in compact regular intervals, since
\(x+1/2\le.72\), \(z+1/2\le.95\), and both sums stay
strictly above zero. There are at most two such rows.
The original unselected Fourier estimate applies because
every type-four target retains its actual negative height.
It supplies exactly the allocations in (7); no finite Fourier
factor is divided out.

**Theorem 2.** For every \(\tau>0\), at both level parities,
\[
 \mathcal B_N(w;x,z)
 \le C_\tau N^{A_\tau}
               \exp N\{\Gamma(z)-1/2000+\tau\}
\tag{25}
\]
uniformly on (3) and on a sufficiently small fixed ordinary-color
neighborhood of \(w=-2\). Every fixed derivative of the cap
with respect to this ordinary color has the same rate on a
smaller neighborhood.

Indeed multiply the complete cap envelope by the low-row bound
(24) and, separately, by each of the at most two half-index
row bounds. Allocate the original weights and use (23) for
each term. Choose all symbol tolerances
within the prescribed \(\tau\). The cap source estimates hold
on the whole real ordinary-color interval. Their five-profile
term has a favorable angular loss, and their true-end term
has a uniform bound on that interval. Discarding the favorable
loss therefore gives the same bound for the complete cap.
Its degree is less than \(N\). The interval
Bernstein--Walsh bound extends the estimate to a sufficiently
small fixed complex neighborhood of \(-2\) at an arbitrarily
small extra exponential cost. Cauchy's formula on a smaller
fixed neighborhood gives the derivative statement. If any
color-independent multiplier in (6) is zero, the bound is
immediate, so this argument needs no division at a zero.

Taking, for example, total tolerance less than \(1/4000\)
leaves a strict joint gap. When this term is attached to the
remaining unselected plateau factors, their original slopes
cancel the remaining marginal in (9). This gives a genuine
suppressed part of the original finite source.

The result does not cover the ordinary indices between the
low cut and the half-index rows, or the indices above those
half-index rows. It does not estimate selected first weights,
the joins of a new outer contour, or the contour where both
first outgoing heights vary. Those contributions must still
be controlled to obtain a whole boundary or whole-word theorem.
No closed-knot or finite-exception conclusion is asserted.

## Frozen direct source versions

| Source | SHA-256 |
|---|---|
| research_mixed_cap_early_fixed_height_full_source.md | d930407eaa5a0bb7c735ee9521c6d352f637124c57c5593cbb1813f069f7d423 |
| research_mixed_first_cap_plateau_completion.md | 4b1a55000a114835ce4b2868b79f4bec63ee781d6d997f7fa6b37f7896e4e87d |
| research_mixed_first_cap_plateau_phase.md | 159a1b89eebcb72fa9ac3395435086f066b3e648c389e2417e0b61fb490ff612 |
| research_mixed_three_row_source_assembly.md | 947fe40bd6125a0bca0f984dc4dde6d55e478ecf0719911829bdb840ef34396c |
| research_mixed_three_left_cut_symmetry_completion.md | 4b75927ad327a47e2e0922a7d9499a6005e6fde0888a9a0e315d997eca8a5a94 |
| research_mixed_four_left_cut_support.md | 5d7dc67647399fd1b3a35a5b3cf26cfd4fe654dd0fed09a4e2d85195c5efae12 |
| research_mixed_first_attached_low_row_transport.md | 8ef728d3808e1480d85a81c1ed8f7eebda99392d0b11f1262e4a47b5a2b196d3 |
| research_mixed_fourier_weight_continuation.md | 0bae41d83f414eb91fd137de1242120a11408147d56ec752e466ca5ed7e7f48e |
| research_mixed_open_word_endpoint_rectangles.md | ac5603badc00d42e98d17a1c5948cae011a6abd991d5249fa61d4224a829ad07 |
| research_mixed_half_row_support_completion.md | 65186e9d2bd3b3275bbcd316f3bf46a28ff8204e3bfcc1cea1939d7ad280e20b |

All needed source statements and their domains were read directly.
The proof uses written inequalities only. No mathematical numerical
evaluation, saved-value arithmetic, import, compilation, test or
frozen-source edit was used.
