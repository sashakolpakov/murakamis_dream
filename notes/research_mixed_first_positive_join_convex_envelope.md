# A complete convex envelope for the first positive-height join

Private written proof, 10 November 2026. At first real coordinate
one tenth, the entire selected first-four pair has an explicit
upper envelope convex in its first height from zero to the
selected height. The second coordinate stays at its actual height.
The envelope retains all cap currents, all ordinary contour
pieces, every physical row and both full Fourier upper branches.
This is convexity of a proved upper envelope, not of the finite
modulus. Its zero-height calibration is a separate source estimate.

## 1. Literal source and fixed domains

Fix an actual positive three/four open word of length at least
three, beginning with four and \(3+\beta\), \(\beta=0,1\).
Retain its reference, logarithmic lifts and scalar. Set
\[
 a=\frac1{10}+ih,\quad 0\le h\le H,\quad 0<H\le\frac7{500},\qquad
 b=z+id,\quad z\in P=[11/50,9/20].
\tag{1}
\]
The actual cap-private height is
\(h_e\in[-.051,-.019]\). For \(\beta=0\) the ordinary-private
height \(h_s\) and \(d\) lie in \([-.065,.068]\); for
\(\beta=1\) they lie in \([-.102,-.001]\). These are containing
bounds on the unchanged actual reference.

With \(q_N=e^{-2\pi i/N}\), \(P_j=(q_N;q_N)_j\), keep
\[
\begin{split}
 U_{1,N}(w,X)&=\sum_{i=0}^{N-1}
       \frac{H_N(w,q_N^{-i})(q_NX;q_N)_i}{P_i^2},\\
 C_{\beta,N}(X,Y)&=\sum_{j=0}^{N-1}
       \frac{X^{-j}(q_NX;q_N)_j(q_NY;q_N)_j}{P_j^{2+\beta}},\\
 \mathcal K_N(w;a,b)&=U_{1,N}(w,X)C_{\beta,N}(X,Y)
                           d_N(X)X^{-N},\\
 X&=e^{-2\pi ia},\qquad Y=e^{-2\pi ib}.
\end{split}
\tag{2}
\]
The outgoing allocation is \(|d_N(Y)|^{\beta/2}\). The coefficient
\(H_N\) is complete. There is no new scalar, discarded row, division
by a finite factor or choice of a square root of \(d_N\).

Use the original bare phases
\[
\begin{split}
 \Psi(e,a)&=S(e)+g(e+a)-g(a)-g(e)
                         -\frac{i\pi}{2}(e-e^2),\\
 Q_\beta(s;a,b)&=g(s+a)+g(s+b)-(2+\beta)g(s)
                         -g(a)-g(b)+2\pi ias,\\
 E_\beta(t;a,b)&=\int_0^t\log|1-e^{-2\pi i(a+v)}|\,dv
       +\int_0^t\log|1-e^{-2\pi i(b+v)}|\,dv\\
       &\hspace{23mm}-(2+\beta)J(t)-2\pi ht,\qquad
                         J(t)=\Re g(t).
\end{split}
\tag{3}
\]
The integrated real-row expression remains defined through all
wrapped and logarithmic-zero rows. In particular
\[
                         E_\beta(1;a,b)=2\pi d_+.
\tag{4}
\]
The identity includes the original first-argument chirp.

## 2. One common complete envelope

Let \(A(h)\) be the maximum of the six cap profiles
\[
\begin{array}{ll}
 \displaystyle\max_{.27\le u\le.49}\Re\Psi(u+ih_e,a),&
 \Re\Psi(.27,a),\quad\Re\Psi(.49,a),\\
 \displaystyle\max_{.27\le u\le.49}\Re\Psi(u-.055i,a)-.11\pi,&
 \displaystyle\max_{.27\le u\le.49}\Re\Psi(u+.04i,a)-.08\pi,\\
 \displaystyle E_{\rm end}(h)=\frac35+2\pi h+\frac{\log4}{100}.&
\end{array}
\tag{5}
\]
The complete independent-height cap theorem, equations (4),
(20)--(21), gives exactly this envelope for type four. Its
additional upper-row allowance is zero. Thus (5) includes all
cap cuts, zero-mode joins, aliases, physical tails and true ends.
We do not restrict the main maximizer to a smaller private interval.

For the ordinary contour put
\[
 \ell_0=\frac3{20},\quad \ell_1=\frac18,\qquad
 y_-=-\frac15,\quad y_{+,0}=\frac15,\quad y_{+,1}=2.
\tag{6}
\]
Define a compact collection of pairs \((s,\omega)\), denoted
\(\mathscr C_\beta\), by the following entire inventory:

| Piece | Private point \(s\) | Penalty \(\omega\) |
|---|---|---|
| Main zero mode | \(v+ih_s,\ \ell_\beta\le v\le1/2\) | \(0\) |
| Both zero-mode joins | \(c+iy,\ c\in\{\ell_\beta,1/2\},\ y\) between \(0,h_s\) | \(0\) |
| Lower horizontal alias | \(v+iy_-,\ \ell_\beta\le v\le1/2\) | \(2\pi\lvert y_-\rvert\) |
| Upper horizontal alias | \(v+iy_{+,\beta},\ \ell_\beta\le v\le1/2\) | \(2\pi y_{+,\beta}\) |
| Four vertical alias halves | \(c+iy,\ c\in\{\ell_\beta,1/2\},\ y\in[y_-,0]\cup[0,y_{+,\beta}]\) | \(2\pi\lvert y\rvert\) |

The real cuts occur in this collection at \(y=0\).
No sign or curvature assertion in the private variable is needed
to discard a piece: none has been discarded. Set
\[
 B_\beta(h,b)=\max\left\{
   \sup_{(s,\omega)\in\mathscr C_\beta}
                  \{\Re Q_\beta(s;a,b)-\omega\},\
   \sup_{1/2\le t\le9/10}E_\beta(t;a,b),\
                  2\pi d_+\right\}.
\tag{7}
\]
The second supremum deliberately retains every high row before
the first numerator wall. It is not replaced by a stationary
branch or inferred from cancellation in a signed sum.

Finally retain the two complete Fourier upper rates:
\[
\begin{split}
 W(h)&=\max\{-\Re g(a)-2\pi h,\ 0\},\\
 q_\beta(b)&=\frac{\beta}{2}
                   \max\{-\Re g(b),2\pi d_+\},\\
 \mathcal E_\beta(h,b)&=A(h)+B_\beta(h,b)+W(h)+q_\beta(b).
\end{split}
\tag{8}
\]
For the actual own-four outgoing height \(d<0\), its last
maximum is the original factorial halfweight. Keeping the maximum
in (8) also states the full general Fourier upper bound explicitly.

**Theorem 1.** For every \(\tau>0\), the literal full source obeys
\[
 |\mathcal K_N(w;a,b)|\,|d_N(Y)|^{\beta/2}
 \le C_\tau N^{A_\tau}
                  \exp N\{\mathcal E_\beta(h,b)+\tau\}
\tag{9}
\]
uniformly on (1), on the whole real ordinary-color interval,
for every integer \(N\ge2\), of either parity. A sufficiently
small fixed ordinary-color
disk about \(-2\) obeys the same statement at any prescribed
additional rate allowance; fixed color derivatives follow on a
smaller disk. For every fixed \(b\), the function
\(h\mapsto\mathcal E_\beta(h,b)\) is convex on \([0,H]\).

## 3. Complete finite-source proof

The cap bound (5) applies on the independent rectangle
\([.1,.22]+i[-.108,.021]\), which contains (1). It is uniform
on the full real ordinary-color interval. All other factors in
(2) are color independent.

Partition the ordinary rows exactly into
\[
 \begin{array}{ll}
 0\le j\le\lfloor N\ell_\beta\rfloor,&\text{low},\\
 \lfloor N\ell_\beta\rfloor+1\le j\le\lceil N/2\rceil-1,
                                                &\text{central},\\
 \lceil N/2\rceil\le j<N,&\text{high}.
 \end{array}
\tag{10}
\]
The exact low-row ratio theorem is uniform on the independent
height box containing (1). Its ratio exceeds \(e^{1/200}\)
up to index \(N/5\), so the first block is bounded by 201
times its final physical row. The continuous rate of that row,
up to the original uniform rounding allowance, is
\(E_\beta(\ell_\beta)=\Re Q_\beta(\ell_\beta)\).
It occurs in (7). This also retains \(j=0\).

For the central block use the original factorial interpolation
and half-grid cuts tending to \(\ell_\beta,1/2\). On the rectangle
in (6) every individual factorial argument stays in a fixed
compact subset of its original strip:
\[
 0<\Re s<1,\quad
 \Re(s+a)\in[.225,.6],\quad
 \Re(s+b)\in[.345,.95],\quad
 \Re a=.1,\quad \Re b\in P.
\tag{11}
\]
For \(\beta=0\) the smaller lower bounds are only improved.
The exact factorial theorem permits arbitrary fixed compact
imaginary-height intervals. Thus its original cotangent
residue formula continues without any pole crossing. The constant
modes give the original \(+N\) real integral. Moving that
zero mode to \(h_s\) retains both unweighted joins. The two
horizontal aliases have penalty \(2\pi|\Im s|\); the four
half-grid vertical halves have the same penalty, including
their height-zero endpoints. These are precisely
\(\mathscr C_\beta\).
This uses the exact contour construction in Section 4 of the
asymmetric-contour theorem, not that theorem's plateau rate
comparison. All terms are bounded directly by (7).

The uniform zero-safe finite-product bounds apply to every
high physical row, with the rate \(E_\beta\) in (3).
For \(1/2\le t\le9/10\) that rate is retained in (7).
For \(9/10\le t\le1\), put \(v=1-t\le1/10\).
The proof of the reflection theorem's Lemma 1 applies directly:
it requires only \(0\le v\le x,z\le1/2\), not its former
plateau lower bound on \(x\). Here \(x=1/10\) and \(z\in P\).
It gives
\[
 E_\beta(1-v)-E_\beta(1)
                  \le\beta J(v)-2\pi d_+v\le0.
\tag{12}
\]
This is a comparison of complete integrated rates, including
product zeros, and not division by a last or half finite row.
The value \(E_\beta(1)\), although the literal last index is
\(N-1\), is a valid upper rate for all these rows. Their number
and the half-grid displacements consume a polynomial and one
arbitrarily small uniform rate tolerance. Both odd half-index
stops and all rows reviving off the grid are retained.

The complete Fourier theorem gives the first rate in (8) for
the whole \(d_N(X)X^{-N}\), and the second for the outgoing
half-modulus. Add the three ordinary blocks, multiply by the
complete cap bound, and allocate the one total tolerance.
This proves (9).
The exact source is polynomial of degree less than \(N\) in its
ordinary color. The Chebyshev estimate in Section 1 of the
horizontal complex-extension theorem, applied to \(w/2\),
therefore gives the stated fixed disks at arbitrarily small
rate allowance. Here the supremum on \([-2,2]\) is bounded
by (9) at the same fixed parameters \(h,b\), so the disk
and its allowance are uniform in those parameters.
Cauchy's formula gives fixed derivatives. No
estimate is continued from a single complete-color value.

## 4. Convexity of every retained height profile

Write
\[
 A_c(h)=\Re\cot\pi(1/10+ih)
       =\frac{\sin(\pi/5)}
                    {\cosh(2\pi h)-\cos(\pi/5)}.
\]
Uniformly for \(0\le h\le7/500\),
\[
                        A_c(h)>\frac{25}{9}.
\tag{13}
\]
Indeed \(2\pi h<9/100\), and the positive cosh series gives
\(\cosh(2\pi h)<101/100\). One may use
\(\cosh t\le1+t^2/[2(1-t^2/12)]\) and \(t^2<1/100\).
The pentagon identities give
\(\cos(\pi/5)>4/5\) and \(\sin(\pi/5)>7/12\).
These yield (13). The latter two inequalities follow from
\(11/5<\sqrt5<9/4\).

For every finite real \(\eta\) and \(1/5\le t<1\),
\[
                 \Re\cot\pi(t+i\eta)\le\frac32.
\tag{14}
\]
For \(t\le1/2\), its value is at most \(\cot\pi t\), by the
explicit denominator formula, and
\(\cot(\pi/5)<3/2\), since
\(\cot^2(\pi/5)=1+2/\sqrt5<2<9/4\).
For \(t\ge1/2\) the real cotangent is nonpositive.
This bound is independent of the private height.

The exact identity \(g''(z)=\pi\cot\pi z-\pi i\) now gives
for every fixed private point occurring in (5) or (7),
\[
\begin{split}
 \partial_h^2\Re\Psi(e,a)
      &=\pi\{A_c(h)-\Re\cot\pi(e+a)\}>0,\\
 \partial_h^2\Re Q_\beta(s;a,b)
      &=\pi\{A_c(h)-\Re\cot\pi(s+a)\}>0.
\end{split}
\tag{15}
\]
Their numerator real parts are at least \(.225>1/5\) and
less than one. The chirp and all fixed alias penalties have
zero second derivative in this *outer* height. In particular
(15) applies to the entire unweighted joining intervals and
the four weighted vertical halves, not only their endpoints.
The true cap-end ceiling is affine for \(h\ge0\).
Taking the specified maxima and suprema therefore proves
convexity of all cap and ordinary contour terms.

For \(1/2\le t<9/10\), the first numerator has not crossed
its real wall. Exact differentiation of its integral gives
\[
 \partial_h^2E_\beta(t;a,b)
       =\pi\{A_c(h)-\Re\cot\pi(a+t)\}>0,
\tag{16}
\]
because \(3/5\le\Re(a+t)<1\), where the second real
cotangent is nonpositive. The second numerator in (3) is
independent of \(h\), even if it has already crossed its own
wall. At \(t=9/10\), continuity of the integrated logarithm
in all parameters gives the pointwise limit of these convex
functions. Hence it is convex there as well, including \(h=0\).
The last-row carrier (4) is constant in \(h\).

Finally
\[
            \partial_h^2\{-\Re g(a)-2\pi h\}
                         =\pi A_c(h)>0.
\tag{17}
\]
The other first Fourier branch is zero. Thus \(W\) is convex,
and \(q_\beta(b)\) is independent of \(h\).
Equations (15)--(17), and closure of convex functions under
sums and suprema, prove the asserted convexity of (8).
No convexity of \(\log|\mathcal K_N|\) has been assumed.

## 5. What this proves about the face, and what it does not

For every fixed \(b\) and \(0\le h\le H\), Theorem 1 gives
the explicit endpoint reduction
\[
 \mathcal E_\beta(h,b)\le
     (1-h/H)\mathcal E_\beta(0,b)
                       +(h/H)\mathcal E_\beta(H,b).
\tag{18}
\]
Here the *same* selected monomial and the complete same-source
envelope occur at both endpoints. At \(H=7/625,\beta=0\),
the individual current and physical-row comparisons in the
completed selected first43 early theorem pay
\(\mathcal E_0(H,b)\) with its stated gap \(1/2000\).
Its proof bounds every high rate before summing, so this
assertion does not infer profile bounds from cancellation.

If the original calibrated plane is denoted \(\Lambda(z)\),
the remaining zero-face sign for this reduction is precisely
\[
                    \mathcal E_\beta(0,z+id)
                                      \le\Lambda(z)-\delta_0.
\tag{19}
\]
A proof only of smallness of the signed full product at
height zero would not establish (19).
An individual-profile proof that bounds all aliases and joins
by the paid main/cut profiles and all high rows by paid
half/last profiles does establish it.
For \(\beta=1,H=1/100\), the corresponding complete selected
first44 source is the separate fixed-height input; Theorem 1
does not assume its calibrated signs to prove the envelope.

Once both endpoint envelopes have strict gaps, (9) and (18)
pay the whole vertical face with the smaller gap, up to the
one prescribed tolerance, and hence pay its literal oriented
integral. This is an application to a concrete full envelope,
not a new saddle-dominance principle.
The second height was never changed. The real segment from
the small old collar to \(x_1=.1\), the unselected negative
first-height join and every other unestimated outer piece
remain separate. No whole-period, whole-word or knot conclusion
is asserted.

## Direct source versions

| Source | SHA-256 |
|---|---|
| research_mixed_cap_early_fixed_height_full_source.md | d930407eaa5a0bb7c735ee9521c6d352f637124c57c5593cbb1813f069f7d423 |
| research_mixed_first_attached_low_row_transport.md | 8ef728d3808e1480d85a81c1ed8f7eebda99392d0b11f1262e4a47b5a2b196d3 |
| research_mixed_right_tail_reflection.md | e3928f2d9549159f6955c654b202dc87198137f4cfdb80f85151af567a976ce1 |
| research_mixed_horizontal_asymmetric_contour.md | 2b0984562d9d3c63e2e366d9dc3b68f557512b71c74290f8ac530fcb4d3e7fce |
| exact_factorial_interpolation_and_complex_contours.md | 1f34f65437dfe0bfb4062a7a74840beae1676353cf13bb8a86f8849a8a36bc72 |
| research_mixed_fourier_weight_continuation.md | 0bae41d83f414eb91fd137de1242120a11408147d56ec752e466ca5ed7e7f48e |
| research_mixed_horizontal_complex_extension.md | c7837a9dfb072f2e276f5ccdb99c7421e154a4ca073a078540d8064dbb3747d4 |
| research_mixed_selected_four_three_early_complete_source.md | c0f4532b7f8d04c3bc4d84f16435029625c469adf1282914f80bf019bd22ebd6 |

The complete written proof and directly used source portions were
read. No mathematical numerical evaluation, saved-value arithmetic,
import, test, compilation or frozen-source edit was performed.
