# The incoming corner with a following three-twist block

Private research proof candidate, 8 November 2026. On the shared
radius range \(13/25<|Y|\le7/10\), the incoming corner can be
estimated with the complete following type-three kernel attached.
The original two sides are used together, with their orientations.
The proof separates the deformation of the first conditional
kernel from the estimate for the following factor.

This note depends on the pointwise profile calibration in
[the type-three right-horizontal theorem](research_mixed_next_three_deep_radius_right_horizontal.md).
It is not adopted until that theorem and this proof have completed
their source and proof reviews. No numerical evaluation is used.

## 1. Domain, finite source, and the two paths

Use the actual ordinary references of types \((3,4,3)\) in
[the complete central theorem](research_mixed_next_own_three_deep_radius_complete_central.md).
Write
\[
\begin{gathered}
(a_*,s_*,y_*,t_*,z_*)=(r_1,s_2^*,r_2,s_3^*,r_3),\\
h_a=\Im a_*,\quad h_s=\Im s_*,\quad h_y=\Im y_*,
\quad h_t=\Im t_*,\quad h_z=\Im z_*,\\
-.072<h_a<0,\qquad -.102<h_s,h_y<-.001,\\
-.108\le h_t\le.068,\qquad -.065<h_z<.068,\\
y=q+ih_y,\quad 0\le q\le11/50,\qquad
z=u+ih_z,\quad u\in P=[11/50,9/20],\\
Y=e^{-2\pi iy},\quad Z=e^{-2\pi iz},\qquad
13/25<R:=|Y|\le7/10 .
\end{gathered}
\tag{1}
\]
The heights retain all their geometric correlations. The first
incoming coordinate varies independently on the rectangle
\[
a=x-i\eta,\qquad 1/2\le x\le7/10,\qquad 0\le\eta\le9/125,
\qquad X=e^{-2\pi ia}.
\tag{2}
\]
At integer level \(N\), put \(r=e^{-2\pi i/N}\),
\(P_j=(r;r)_j\), and \(p_j(V)=(rV;r)_j\). The two kernels are
\[
C_{\beta,N}(V,W)=
 \sum_{j=0}^{N-1}\frac{V^{-j}p_j(V)p_j(W)}{P_j^{2+\beta}},
\qquad \beta=0,1.
\tag{3}
\]
In the present calculation the first kernel is \(C_{1,N}\) and
the following kernel is \(C_{0,N}\). Keep the complete cap
\(U_{0,N}(w,X)\), with real ordinary color \(w\in[-2,2]\), and
the original degree-\((N-1)\) Fourier polynomial \(d_N\), characterized
by \(d_N(r^b)=P_b^{-1}\). Set
\[
D_N(a)=U_{0,N}(w,X)C_{1,N}(X,Y)d_N(Y)C_{0,N}(Y,Z).
\tag{4}
\]
There is no outgoing halfweight for this following type.

Let \(a_L=1/2+ih_a\). The old and replacement paths are
\[
\begin{split}
\Gamma_{\rm old}&=[a_L,1/2]\ \cup\ [1/2,7/10],\\
\Gamma_{\rm new}&=[a_L,7/10+ih_a]\ \cup\ [7/10+ih_a,7/10].
\end{split}
\tag{5}
\]
Each segment is oriented from its first endpoint to its second.
Let \(\Lambda_{123}(z)\) retain the reference action bound from
the complete central theorem.

**Theorem.** On the actual reference domain (1), for both level
parities and all real ordinary colors,
\[
 |D_N(a)|\le CN^B e^{N\{\Lambda_{123}(z)-10^{-10}\}},
 \qquad a\in\Gamma_{\rm new}.
\tag{6}
\]
Consequently,
\[
 \left|N\int_{\Gamma_{\rm old}}D_N(a)\,da\right|
 \le CN^B e^{N\{\Lambda_{123}(z)-10^{-10}\}}.
\tag{7}
\]
This asserts a bound for the combined old path, not separate
absolute bounds for its two segments. No derivative conclusion
for (6)--(7) is asserted.

## 2. The first conditional deformation is independent of the following type

Use the original primitive \(g\), including its additive constant,
and the first phase
\[
Q(s;a,y)=g(a+s)+g(y+s)-3g(s)-g(a)-g(y)+2\pi ias.
\tag{8}
\]
Let \(s_c(a,y)\) be its original zero-lift critical point and put
\(\Theta(a,y)=Q(s_c(a,y);a,y)\), \(M(a,y)=\Re\Theta(a,y)\).
The [root annulus](research_mixed_conditional_corner_root_annulus.md)
and [real-coordinate guard](research_mixed_conditional_corner_root_angle.md)
apply to the entire rectangle (2) and the closed shared interval
in (1). Their statements concern only \(a,y\), and give
\[
 Q_s(s_c;a,y)=0,\qquad
 2/25<\Re s_c<1-\Re a,\qquad
 |\Im s_c|<\frac{\log2}{2\pi}.
\tag{9}
\]
The root is simple and the original logarithmic branch persists
at \(q=0\).

We extract the part of
[the lower-left Gaussian deformation](research_mixed_next_lower_left_corner_gaussian_deformation.md)
that concerns the first kernel alone. There is an actual local
integral \(G_N(a,y)\), with its original orientation, such that
\[
 G_N=N^{-1}\mathcal B(a,y)e^{N\Theta(a,y)}
          (1+O_{\rm hol}(N^{-1})),\qquad \mathcal B\ne0,
\tag{10}
\]
and, writing \(B_0=2383/1500\), for every \(\tau>0\),
\[
\begin{split}
 |U_{0,N}(w,X)\{C_{1,N}(X,Y)-G_N(a,y)\}|
 \le {}&C_\tau N^{B_\tau}|U_{0,N}(w,X)|
                         e^{N(M-\gamma)}\\
       &+C_\tau N^{B_\tau}e^{N(B_0+\tau)}
\end{split}
\tag{11}
\]
for a uniform \(\gamma>0\). Here and below a finite compact
cover of the original parameter family supplies uniform constants.

To justify (11) without transferring a following-type hypothesis,
retain the exact first-kernel cuts
\[
L_N=\lfloor2N/25\rfloor+1,\quad M_N=\lceil N/2\rceil,\quad
\ell_N=(L_N-\tfrac12)/N,\quad b_N=(M_N-\tfrac12)/N .
\]
The [corner middle reduction](research_mixed_next_lower_left_corner_middle_reduction.md),
equations (5)--(6), proves
\[
 C_{1,N}(X,Y)=N\int_{\ell_N}^{b_N}T_N(s;a,y)\,ds+\mathcal E_N,
 \qquad |U_{0,N}\mathcal E_N|
 \le C_\tau N^{B_\tau}e^{N(B_0+\tau)} .
\tag{12}
\]
Its proof through Section 5 uses only \(a,y,w\).
It includes all physical rows outside the cuts, both horizontal
Fourier remainders and four weighted vertical pieces. The low
and upper physical bounds are respectively \(B_0\) and
\(32563/21000<B_0\); the two horizontal error rates are less
than \(13/10<B_0\). None uses \(z,h_t,h_z\).

Sections 2--3 of the Gaussian deformation move the middle integral
to the height of (9). The root and curvature estimates again use
only \(a,y\). In particular their postwall inequalities require
\(|Y|\le1\), not any restriction on the following type. The
critical-height line has a unique maximum \(M\); its complement
outside a fixed regular critical chart has rate at most
\(M-\gamma\), after reducing \(\gamma>0\) if necessary.

Both unweighted connecting sides remain. At the lower cut their
rate is bounded by the larger endpoint rate by vertical convexity.
At the half cut the continuous rate decreases up to height
\(\eta\) and increases thereafter, so the same endpoint conclusion
holds. The critical-height endpoints have rate at most
\(M-\gamma\). Multiplication of either real-cut rate by the
complete cap gives at most \(B_0\), with any prescribed tolerance.
Uniform continuity of the integrated rate covers the half-grid
shifts, including the different even and odd cutoffs.
These are exactly the first-kernel statements of Section 4 of
the Gaussian deformation; its subsequent type-four attachment
is not used here. Adding these bounds to (12) proves (11).

The local integral (10) uses the original regular factorial symbol.
At \(q=0\), its unshifted \(y\)-factor has the previously proved
inward-seam continuation. Thus its coefficient and its factor
\(N^{-1}=N\cdot N^{-3/2}\cdot N^{-1/2}\) are unchanged.
No nonzero coefficient for the full transfer is inferred from (10).

## 3. Calibration at the left corner endpoint

Put \(A=\Re a_*\), \(\kappa_0=1/2500000\), and retain the
original cap supporting rate
\[
B_U(x)=\Re T_0(a_*)-\Re p_L(x-A)-\kappa_0(x-A)^2,\qquad
B_*=B_U(1/2).
\tag{13}
\]
The attached equation is \(T_0'(a_*)+p_L=0\).
For the following type-three phase and physical rate write
\[
\begin{split}
Q_0(t;y,z)&=g(y+t)+g(z+t)-2g(t)-g(y)-g(z)+2\pi iyt,\\
E_0(t;y,z)&=\int_0^t\log|1-Ye^{-2\pi ib}|\,db
 +\int_0^t\log|1-Ze^{-2\pi ib}|\,db
 -2J(t)-2\pi h_yt,\qquad J(t)=\Re g(t).
\end{split}
\tag{14}
\]
Define the following set of real rates:
\[
\begin{split}
\mathscr P_0(y,z)= {}&
\{\Re Q_0(t_R+ih_t;y,z):3/20\le t_R\le1/2\}\\
&{}\cup\{E_0(3/20;y,z),E_0(1/2;y,z),L_0\}\\
&{}\cup\{E_0(t;y,z):1/2\le t\le4/5-q\},
\quad L_0=-\log R+2\pi(h_z)_+ .
\end{split}
\tag{15}
\]
The last interval is nonempty throughout (1).
The complete next-current and low-row results control the lower
half by the first two groups. The upper physical rate reduction
in [the complete central theorem](research_mixed_next_own_three_deep_radius_complete_central.md)
controls all other upper indices by \(L_0\) and
\(E_0(4/5-q;y,z)\). Therefore
\[
 |C_{0,N}(Y,Z)|\le C_\tau N^{B_\tau}
       \exp N\{\max_{\varphi\in\mathscr P_0(y,z)}\varphi+\tau\}.
\tag{16}
\]
This bound retains every row, both horizontal Fourier remainders,
all weighted sides, and both unweighted joins. It is an upper
bound, valid also when a numerator vanishes.

The pointwise calibration of
[the right-horizontal theorem](research_mixed_next_three_deep_radius_right_horizontal.md)
at \(a=a_L\) states, for every \(1/20\le s_R\le1/2\) and
\(\varphi\in\mathscr P_0(y,z)\),
\[
 B_*+\Re Q(s_R+ih_s;a_L,y)+\varphi-\Re g(y)
 <\Lambda_{123}(z)-10^{-9}.
\tag{17}
\]
This uses the original cap quadratic loss and the original
own-three supporting bound, including the positive-height term
in \(L_0\). It is a phase-by-phase assertion; a bound on the
coherent finite product alone would not imply (17).

At \(a=a_L\) the first numerator wall is at real index \(1/2\).
Let \(\widehat R\) denote the original continuous first-row rate,
equal to \(\Re Q\) before that wall, and set
\[
m(\sigma)=\max_{2/25\le v\le1/2}
                    \widehat R(v,\sigma;a_L,y).
\tag{18}
\]
The [prewall curvature theorem, Section 5](research_mixed_next_lower_left_corner_prewall_curvature.md)
makes \(m\) convex on \(|\sigma|\le\log2/(2\pi)\), with its
minimum at the height of \(s_c(a_L,y)\). Both this height and
the original \(h_s\) lie in the interval. Thus
\[
\Re\Theta(a_L,y)\le m(h_s).
\tag{19}
\]
The next rate \(\varphi\) is fixed while the first maximum is
taken. Since the interval in (18) is contained in the first-index
range of (17), equations (17)--(19) imply
\[
 B_*+\Re\Theta(a_L,y)+\varphi-\Re g(y)
 <\Lambda_{123}(z)-10^{-9}
 \quad(\varphi\in\mathscr P_0(y,z)).
\tag{20}
\]

## 4. Transport along the replacement path and finite error bounds

The cap-only estimate of
[the selected incoming corner, equation (18)](research_mixed_next_selected_incoming_corner_union.md)
has rate at most \(B_*+\tau\) along the bottom side of
\(\Gamma_{\rm new}\). It is independent of the following type.
On the right side the
[seven-tenths cap estimate](research_mixed_cap_seven_tenths_vertical_bound.md)
has rate \(3907/4500<7/8<B_*\), by
[the original cap-plane floor](research_mixed_next_calibrated_cap_plane_floor.md).
Hence on both sides
\[
 |U_{0,N}(w,X)|\le C_\tau N^{B_\tau}e^{N(B_*+\tau)}.
\tag{21}
\]
These estimates include all real ordinary colors.

The [algebraic action theorem](research_mixed_four_conditional_algebraic_transport_domain.md)
gives \(\Re\Theta_a<0\), \(\Im\Theta_a>0\) for \(q>0\)
on (2). Its hypotheses concern only \(a,y\).
At \(q=0\) the annulus theorem continues the same derivative,
so the weak limiting inequalities suffice. Moving first rightward
and then upward gives
\[
 \Re\Theta(a,y)\le\Re\Theta(a_L,y),
 \qquad a\in\Gamma_{\rm new}.
\tag{22}
\]
No new strict loss is needed.

The original forced Fourier bound, valid through \(q=0\), is
\[
 |d_N(Y)|\le C_\tau N^{B_\tau}e^{N\{-\Re g(y)+\tau\}}.
\tag{23}
\]
Combining (16), (20)--(23), with the total tolerance smaller
than half the reserve in (20), proves
\[
 |U_{0,N}(w,X)d_N(Y)C_{0,N}(Y,Z)|e^{N\Re\Theta(a,y)}
 \le CN^B e^{N\{\Lambda_{123}(z)-\tfrac12\,10^{-9}\}}.
\tag{24}
\]
The original Fourier polynomial is not replaced by a homogeneous
reciprocal-factorial continuation in this step.

To attach the second error in (11), use
[the type-three attachment theorem](research_mixed_next_three_deep_radius_bounded_prefix.md).
Taking the particular preceding factor \(V_N=e^{NB_0}\) in
that theorem gives
\[
 |d_N(Y)C_{0,N}(Y,Z)|
 \le CN^B e^{N\{\Lambda_{123}(z)-B_0-1/200\}}.
\tag{25}
\]
Choose the tolerance in the second term of (11) smaller than
\(1/1000\). After multiplication by (25), that term has deficit
greater than \(1/250\); the weaker deficit \(1/1000\) is sufficient.
This deduction uses an absolute upper bound. It neither divides
by the possibly vanishing cap nor assigns a signed-sum estimate
to individual rows.

The first error in (11) is bounded by (24), with its additional
factor \(e^{-N\gamma}\). The local term (10) is bounded directly
by (24). Adding these terms and the second error proves (6);
the conservative deficit \(10^{-10}\) absorbs the polynomial
prefactors and fixed finite additions.

For each fixed \(N,w,y,z\), \(D_N(a)\) is entire in \(a\):
its \(a\)-dependent factors are finite Laurent polynomials in
\(e^{-2\pi ia}\), which never vanishes at finite \(a\).
Cauchy's theorem therefore gives the exact oriented identity
\[
 N\int_{\Gamma_{\rm old}}D_N(a)\,da
 =N\int_{\Gamma_{\rm new}}D_N(a)\,da.
\tag{26}
\]
Both replacement path lengths are bounded independently of \(N\).
Equation (6) proves (7), with the original factor \(+N\) retained.

## 5. What this permits in the larger proof

The estimate includes the combined incoming corner and the complete
following type-three sum on (1). It can be assembled with the
initial, tapered, central, right-horizontal and far-real incoming
pieces when their hypotheses are verified on the same reference
family. That assembly must retain the shared Fourier filter and
its denominator.

The range \(R>7/10\), the other shared-variable contours, and the
noncancellation of the complete transfer are separate problems.
The local nonzero coefficient in (10) does not resolve them.
