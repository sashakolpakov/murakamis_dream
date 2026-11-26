# Localizing both low-cardinal Fourier contributions together

Research deduction, 7 November 2026. The two Fourier contributions of
the low physical input interval can be removed together from the
complement of their central segments. The complete low physical sum
is already small. Here the unselected central segment is also bounded,
using the original ordinary conditional source and its affine
marginal; the selected central segment has an existing bound.
Subtracting both segments from the exact complete sum then bounds
the sum of their complements.

The complementary contours need not coincide. No estimate for either
complete Fourier contribution separately is asserted. The conclusion
is at the actual ordinary next-output references and their fixed
local neighborhoods, not at every independent outgoing plateau
coordinate. No numerical evaluation is used.

## 1. Exact input, coefficients, and contour orientations

Put \(D=N-1\), \(q=e^{\pi i/N}\), \(r=q^{-2}\),
\(\kappa=q^{D^2/2}\), \(P_j=(r;r)_j\), and \(p_j(Y)=(rY;r)_j\).
Retain the complete prefix \(F_N=F_{34,N}\) and

\[
 C_{\beta,N}(Y,Z)=\sum_{j=0}^{D}
       \frac{Y^{-j}p_j(Y)p_j(Z)}{P_j^{2+\beta}},
 \qquad
 d_N(r^b)=P_b^{-1},\quad \deg d_N\le D,\quad \beta=0,1.
 \tag{1}
\]

Choose the fixed low interval of
[the low physical interval theorem](research_mixed_next_low_physical_interval.md):

\[
 I_N=\{0,\ldots,\lfloor\delta N\rfloor\},\qquad
 \mathfrak l_b(Y)=\frac1N\sum_{\nu=0}^{D}(Yr^{-b})^\nu,\qquad
 E_N(w,Y)=\sum_{b\in I_N}F_N(w,r^b)\mathfrak l_b(Y).
 \tag{2}
\]

The constant \(\delta<1/40\) is chosen sufficiently small as in that
theorem. Its two exact Fourier contributions are

\[
 \mathcal S_{\sigma,\beta}[E_N](w,Z)
      =N[Y^{\sigma N}]\{E_N(w,Y)d_N(Y)C_{\beta,N}(Y,Z)\},
 \qquad \sigma=0,1.
 \tag{3}
\]

The product in braces has band \([-D,2D]\). Therefore their sum,
without an additional root-average multiplier, is

\[
 \mathcal T_\beta[E_N](w,Z)
 :=\mathcal S_{0,\beta}[E_N]+\mathcal S_{1,\beta}[E_N]
 =\sum_{b\in I_N}\frac{F_N(w,r^b)}{P_b}C_{\beta,N}(r^b,Z).
 \tag{4}
\]

Every row in (1) and every zero at a physical input remains.
In the original matrix normalization the resulting conditional
message is multiplied, at a physical outgoing index \(k\), by
\(\kappa^{4+\beta}N^{1+\beta}P_k^{1-\beta}\), exactly as in
[the next-source identity, equation (3)](research_mixed_three_four_next_local_source.md).
No final Gram factor is inserted here.

For each \(\sigma\), let \(\Gamma_\sigma\) be a fixed, piecewise
smooth path in the logarithmic \(y\)-cylinder making one increasing
period, with \(Y=e^{-2\pi iy}\). It represents one clockwise circuit
about \(Y=0\). The coefficient orientation is

\[
 \mathcal S_{\sigma,\beta}[E_N]
  =N\int_{\Gamma_\sigma}
       E_N(w,Y)d_N(Y)Y^{-\sigma N}C_{\beta,N}(Y,Z)\,dy.
 \tag{5}
\]

Indeed \(dY/(2\pi iY)=-dy\); the clockwise orientation cancels
that minus sign. All such deformations are exact for the finite
Laurent integrand. In particular the two paths may have different
heights and different connecting pieces.

## 2. The actual references and an unselected central bound

Use the ordinary-next canonical family of
[the selected plateau comparison](research_mixed_next_filtered_selected_plateau.md):

\[
 (a_*,s_*,y_*,t_*,z_*)=(r_1,s_2^*,r_2,s_3^*,r_3),\qquad
 (\epsilon_1,\epsilon_2,\epsilon_3)=(0,1,\beta),\qquad
 c=s_4^*\in K_3\cup K_4.
 \tag{6}
\]

Both subsequent blocks are ordinary, also when the original word
has length four. In particular \(s_*,y_*\in O_4\), so

\[
 .24<\Re s_*,\Re y_*<.36,\qquad
 -.102<\Im s_*,\Im y_*<-.001.
 \tag{7}
\]

Set \(P=[.22,.45]\), \(h_*=\Im y_*\), \(H=1/100\), and

\[
 \begin{split}
 \gamma_0&=P+ih_*,&\gamma_1&=P+iH,\\
 z&=u+i\Im z_*,&&u\in P.
 \end{split}
 \tag{8}
\]

Both central segments have increasing orientation. The variables
\(b\) in (2) and \(u\) in (8) are respectively a physical input
index and an independent outgoing real coordinate.

Retain the original action and marginals from equations (7)--(8)
of the selected plateau comparison:

\[
 \begin{split}
 Q_\beta(t;y,z)
   &=g(t+y)+g(t+z)-(2+\beta)g(t)-g(y)-g(z)+2\pi iyt,\\
 A_*&=\Re\{\mathcal P_{34}(-2,y_*)-\tfrac12g(y_*)\},\\
 p&=\Re\{g'(s_*+y_*)-\tfrac32g'(y_*)\},\\
 p_R&=g'(t_*+z_*)-(1+\beta/2)g'(z_*),\\
 \Lambda_{123}(z)
   &=\Re\{\mathcal P_{34}(-2,y_*)+Q_\beta(t_*;y_*,z_*)
                         -g(y_*)-\tfrac\beta2g(z_*)\}
          +\Re\{p_R(z-z_*)\}.
 \end{split}
 \tag{9}
\]

All primitives and additive constants are unchanged.

**Lemma 1.** On the whole independent plateau in (8), the unselected
central density satisfies

\[
 |E_N(w,Y)d_N(Y)C_{\beta,N}(Y,Z)|\,|d_N(Z)|^{\beta/2}
 \le C_\tau N^{A_\tau}
       e^{N\{\Lambda_{123}(z)-1/20+\tau\}},\qquad y\in\gamma_0.
 \tag{10}
\]

This holds for both parities, all real ordinary colors, and a
sufficiently small fixed complex disk about \(w=-2\).

*Proof.* The exact coefficient identity and the low coefficient
theorem give

\[
 F_N(w,r^b)=\frac{(-q)^bP_b}{\kappa^2N}\ell_{b,N}(w),
 \qquad
 |\ell_{b,N}(w)|
 \le C_\tau N^{A_\tau}
       e^{N\{M_{\rm pend}+\epsilon(\delta)+\tau\}},
 \quad M_{\rm pend}<769/500.
 \tag{11}
\]

These are complete coherent coefficients. Since \(\delta<1/6\),
each factor in \(|P_b|\) is at most one on this index range.
Also \(|\mathfrak l_b(Y)|\le1\) on \(|Y|\le1\). The fixed
allowances in the low interval theorem are small enough to give

\[
             \sup_{|Y|\le1}|E_N(w,Y)|\le CN^A e^{77N/50}.
 \tag{12}
\]

There is a strict reserve \(77/50-769/500=1/500\); no limiting
zero-tolerance assertion is needed.

Write \(\nu(y)=-\Re g(y)\). On \(x\in P\) and \(h\le0\) the
original logarithmic lift satisfies

\[
 \partial_h\nu(x+ih)=\arg(1-e^{2\pi h-2\pi ix})>0.
 \tag{13}
\]

The real part of this logarithm's argument is positive and its
imaginary part is positive. Consequently
\(\nu(x+ih)\le\nu(x)=-J(x)\), where \(J=\Re g\) on the real
interval. The full polynomial bound in
[Fourier weight continuation, Section 5](research_mixed_fourier_weight_continuation.md)
keeps both its factorial and forcing terms and yields

\[
 |d_N(Y)|^{1/2}\le C_\tau N^{A_\tau}
               e^{N\{-J(x)/2+\tau\}},\qquad y=x+ih_*.
 \tag{14}
\]

Here \(J(x)<0\) on \(P\), so the forcing alternative of rate zero
is included. No division by \(d_N\) is made.

Let \(B_3(x,u)\) be the complete ordinary third-factor plane.
[Three-row source assembly, Theorem 1, equation (6)](research_mixed_three_row_source_assembly.md)
applies with first external flag \(\eta=1\) and own flag \(\beta\):

\[
 |C_{\beta,N}(Y,Z)|\,|d_N(Y)|^{1/2}|d_N(Z)|^{\beta/2}
 \le C_\tau N^{A_\tau}e^{N\{B_3(x,u)+\tau\}}.
 \tag{15}
\]

Its inputs are the actual ordinary family (6), and its target
heights are their actual heights. The sufficient typed products
and the half-chain interpretation are also checked in
[the unselected interior theorem, Section 2](research_mixed_retained_prefix_unselected_plateau.md).
Thus (15) includes every conditional row, both physical ends,
revived rows and all finite contour currents. There is no
selected-height allowance in (15).

Original stationarity and the halfweight allocation give

\[
 A_*+p(x-a)+B_3(x,u)\le\Lambda_{123}(z),\qquad
 a=\Re y_*,\qquad A_*>\frac74+\frac{819}{35200}.
 \tag{16}
\]

These are precisely equations (18)--(19) of the selected plateau
comparison. It remains to bound

\[
                   \frac{77}{50}-\frac{J(x)}2-p(x-a)-A_*.
 \tag{17}
\]

The following marginal estimates were proved in its equations
(23)--(29), using only (7) and the original logarithms. If \(p\le0\),
put \(k(a)=\tfrac32\log(2\sin\pi a)\). Then

\[
 -p\le k(a),\qquad k(a)>\tfrac12\log2,\qquad
                       k(a)(.45-a)<3/25.
 \tag{18}
\]

Let \(H_-(x)=-J(x)/2\). It is at most \(1/12\), and
\(H_-'(x)\ge-\tfrac12\log2\). For \(x<a\), the marginal term
in (17) only improves that bound. For \(x\ge a\),
\(H_-(x)+k(a)(x-a)\) is increasing, so

\[
 H_-(x)-p(x-a)
 \le\max\{1/12,\ H_-(.45)+3/25\}
 <\max\{1/12,\ 7/400+3/25\}=\frac{11}{80}.
 \tag{19}
\]

We used \(H_-(.45)<\log2/40<7/400\).
Thus (17) is smaller than
\(77/50+11/80-7/4=-29/400<-1/20\).

If \(p\ge0\), the same source comparison proves
\(p(a-.22)<801/10000\). Therefore

\[
 \frac{77}{50}+H_-(x)-p(x-a)
 \le \frac{77}{50}+\frac1{12}+\frac{801}{10000}
       =\frac{51103}{30000}.
 \tag{20}
\]

The difference between \(7/4\) and (20) is \(1397/30000\).
Since \(819/35200>1/50\), (16) leaves more than
\(1997/30000>1/20\). Both cases prove (10), after sharing the
arbitrarily small finite tolerances. \(\square\)

The same proof works for any degree-\(D\) polynomial satisfying
(12). This assertion concerns an absolute upper bound, not a
substitution of a new leading amplitude for the original prefix.

## 3. The two central integrals and the complementary sum

Choose each \(\Gamma_\sigma\) in (5) to contain its respective
segment \(\gamma_\sigma\), and define

\[
 \begin{split}
 G_{\sigma,\beta,N}(w,z)
   &=N\int_{\gamma_\sigma}
       E_N(w,Y)d_N(Y)Y^{-\sigma N}C_{\beta,N}(Y,Z)\,dy,\\
 R_{\sigma,\beta,N}(w,z)
   &=N\int_{\Gamma_\sigma\setminus\gamma_\sigma}
       E_N(w,Y)d_N(Y)Y^{-\sigma N}C_{\beta,N}(Y,Z)\,dy.
 \end{split}
 \tag{21}
\]

The second line means the oriented remaining chain, including all
connecting pieces. For example \(\Gamma_\sigma\) may simply be
the complete horizontal period at the height of \(\gamma_\sigma\).
It may instead be any previously chosen exact finite-source cycle
containing that segment. Its paths, endpoints and heights are
held fixed at the base reference when outside parameters vary.

For \(G_0\), Lemma 1 gives the whole independent outgoing-plateau
bound (10), with the extra scalar \(N\) costing only a power.
For \(G_1\), the proof of
[the selected plateau theorem](research_mixed_next_filtered_selected_plateau.md),
Sections 3--5, applies to \(E_N\): it uses only degree at most
\(D\) and (12), not the additional high-node or first-coordinate
terms in that theorem's correction. It gives

\[
 |G_{1,\beta,N}(w,z)|\,|d_N(Z)|^{\beta/2}
 \le C_\tau N^{A_\tau}
             e^{N\{\Lambda_{123}(z)-1/500+\tau\}}
 \quad(z=u+i\Im z_*,\ u\in P).
 \tag{22}
\]

Both the factorial and polynomial-forcing alternatives of the exact
selected weight are retained.

For the following conclusion restrict to the actual \(z_*\) and
sufficiently small fixed neighborhoods of it. Let
\(\mathcal P_\beta^+(w,z)\) be the original next conditional action
of the local next-source theorem. At the complete-color reference,

\[
       \Lambda_{123}(z_*)=
       \Re\mathcal P_\beta^+(-2,z_*)-\frac{\beta}{2}\Re g(z_*).
 \tag{23}
\]

For \(\beta=1\), \(z_*\in O_4\), and the actual nonzero
factorial asymptotic for \(d_N(Z)\) on this compact family is
[Fourier weight continuation, Corollary 2](research_mixed_fourier_weight_continuation.md).
Consequently the outgoing halfweight in (10), (22), and (23)
cancels on these neighborhoods, with polynomial factors retained.
For \(\beta=0\) there is no outgoing halfweight. Strict gaps,
the fixed-base complex source extension and continuity therefore
give unweighted bounds for \(G_0,G_1\) relative to
\(\Re\mathcal P_\beta^+(w,z)\). The available normalized fixed-jet
gaps may be taken as \(1/200\) and \(1/2000\), respectively,
after shrinking the neighborhoods.

Now put \(\Delta=59/440000\), as in the low physical interval
theorem. That theorem gives, on the same smaller neighborhoods,

\[
 \partial_w^j\partial_z^k
 \left(e^{-N\mathcal P_\beta^+(w,z)}
                  \mathcal T_\beta[E_N](w,e^{-2\pi iz})\right)
                          =O_{j,k}(e^{-N\Delta/4}).
 \tag{24}
\]

Its all-real ordinary-color positive estimate also holds; it is
calibrated against the complete-color action. It does not require
any separate bound for a Fourier contribution.

**Theorem 2.** Uniformly on the ordinary-next reference family (6),
both parities, and sufficiently small fixed complete-color and
output neighborhoods, the sum of the two complementary integrals
obeys

\[
 \partial_w^j\partial_z^k
 \left[
 e^{-N\mathcal P_\beta^+(w,z)}
       \{R_{0,\beta,N}(w,z)+R_{1,\beta,N}(w,z)\}
 \right]
                     =O_{j,k}(e^{-N\Delta/8})
 \quad(j,k\text{ fixed}).
 \tag{25}
\]

For all real ordinary colors, the same sum, and every fixed
ordinary derivative, has an absolute exponential bound with the
complete-color normalization
\(\Re\mathcal P_\beta^+(-2,z)\), on suitably smaller fixed output
neighborhoods. No normalized logarithmic derivative in the ordinary
color is asserted away from complete color.

*Proof.* Equations (4), (5), and (21) give the exact identity

\[
 \boxed{\quad
 R_{0,\beta,N}+R_{1,\beta,N}
      =\mathcal T_\beta[E_N]-G_{0,\beta,N}-G_{1,\beta,N}.
 \quad}
 \tag{26}
\]

The contours on the two sides have not been identified. Each
central segment was subtracted from its own complete coefficient
cycle. Apply (24) and the two central bounds to (26).
All finite scalar and differentiation costs are polynomial;
the displayed smaller exponent absorbs them. For real ordinary
derivatives, apply Markov to the complete coefficient polynomials
before the finite cardinal sum, using (11). For complex mixed
derivatives keep all base paths fixed and apply Cauchy on nested
neighborhoods. This proves (25) and the all-real assertion.
\(\square\)

Thus replacing \(F_N\) by \(F_N-E_N\) changes the sum of the two
complements by an exponentially small quantity, while both central
segments also change by exponentially small quantities. This
removes the need to prove independent complete-sector suppression
of this low-cardinal correction in a local next-source assembly.
It does not estimate the complementary source of \(F_N-E_N\), nor
claim a complete \(343\) or \(344\) asymptotic.

## 4. The exterior formula and its pole

The precise pole bookkeeping can also be seen directly. Put

\[
 W_N(w,Y)=\sum_{b\in I_N}(-q)^b\ell_{b,N}(w)P_b
                                     \frac{r^b}{Y-r^b}.
 \tag{27}
\]

The cardinal formula and (11) give the rational identity

\[
                E_N(w,Y)=\frac{Y^N-1}{\kappa^2N^2}W_N(w,Y).
 \tag{28}
\]

The right side is the polynomial (2); its apparent poles cancel.
On an open arc the original unselected and selected densities
therefore contain, respectively, the additional factors
\(Y^N-1\) and \(1-Y^{-N}\) multiplying \(W_Nd_NC_\beta\).
Their moduli are at most two on the inside and outside central
arcs, respectively. They are not identically one on those arcs.
The central proofs above used the original polynomial \(E_N\)
directly, so neither factor was discarded there.
For \(\rho<1<R\), with both circles counterclockwise, exact
Laurent bands give

\[
 \begin{split}
 \mathcal S_{0,\beta}[E_N]
    &=-\frac1{\kappa^2N}\frac1{2\pi i}
       \oint_{|Y|=\rho}\frac{W_N(w,Y)d_N(Y)C_{\beta,N}(Y,Z)}Y\,dY,\\
 \mathcal S_{1,\beta}[E_N]
    &=\frac1{\kappa^2N}\frac1{2\pi i}
       \oint_{|Y|=R}\frac{W_N(w,Y)d_N(Y)C_{\beta,N}(Y,Z)}Y\,dY .
 \end{split}
 \tag{29}
\]

Inside the unit circle \(W_N\) has only nonnegative powers, so the
\(Y^N\) term in the first line of (28) has no constant coefficient
after multiplication by \(d_NC_\beta\), whose lowest degree is
\(-D\). Outside, \(W_N\) starts at \(Y^{-1}\), so the extra
\(Y^{-N}\) term in the selected expression has no constant
coefficient either. These observations prove (29) without replacing
a finite Fourier sum by point sampling.

The residue at a physical pole \(B=r^b\) of the unscaled integrand
in (29) is

\[
 (-q)^b\ell_{b,N}(w)P_b\,d_N(B)C_{\beta,N}(B,Z)
       =(-q)^b\ell_{b,N}(w)C_{\beta,N}(B,Z).
 \tag{30}
\]

After multiplication by \(1/(\kappa^2N)\), their sum is exactly
(4). In particular the \(B=1\) residue is genuine. Dropping it
when splitting a divided difference would change the source.
Moving both contours of (29) to a common contour cancels their
remaining integrals and leaves precisely these residues. Equation
(26), however, proves the localized result even when the prescribed
central segments and their complements lie on different contours.

## 5. The complete correction for the \(11/12\) physical cutoff

The same argument applies to the entire filtered polynomial in
[the low physical interval theorem, Section 4](research_mixed_next_low_physical_interval.md).
Keep its specific upper cutoff \(B_N=\lceil11N/12\rceil\), and put

\[
 \begin{split}
 I_N^{\rm end}&=I_N\cup\{B_N,\ldots,D\},&
 \Pi_{\rm end}F&=\sum_{b\in I_N^{\rm end}}F(r^b)\mathfrak l_b,\\
 F_N^{\rm mid}&=(I-\Pi_{\rm end})(F_N-R_N^a),&
 E_N^{\rm all}&=F_N-F_N^{\rm mid}
        =R_N^a+\Pi_{\rm end}F_N-\Pi_{\rm end}R_N^a .
 \end{split}
 \tag{31}
\]

Here \(R_N^a\) is the original first-coordinate deletion
\(a\ge A_N=\lceil23N/24\rceil\), not a restriction of a continuous
first-coordinate arc.

**Corollary 3.** Lemma 1 and (22) hold with \(E_N^{\rm all}\)
in place of \(E_N\). At the actual ordinary output references and
their fixed local neighborhoods, Theorem 2 holds with the two
complementary integrals of \(E_N^{\rm all}\) as well.
Consequently the replacement \(F_N\mapsto F_N^{\rm mid}\)
preserves each central contribution and the sum of the two
complementary contributions up to the stated exponentially small
errors. The all-real color and fixed-derivative scopes are unchanged.

*Proof.* Section 2, equations (10)--(12), of
[the selected plateau comparison](research_mixed_next_filtered_selected_plateau.md)
proves

\[
       \sup_{|Y|\le1}|E_N^{\rm all}(w,Y)|\le CN^A e^{77N/50}.
 \tag{32}
\]

For completeness, its high-node rate is
\(433/500+85/288+17/60+7/120=54101/36000<77/50\);
its low-node rate is (11). Both \(R_N^a\) and its cardinal
projection have rate \(371/720\). Thus (32) retains strict
allowances and all its all-real and complex-color conclusions.
The degree is at most \(D\). Lemma 1 is applicable by its last
paragraph, and the selected estimate follows from (22).

The complete transfer of \(E_N^{\rm all}\) is the exact error in
reducing the physical double sum to

\[
       0\le a<A_N,\qquad
        \lfloor\delta N\rfloor<b<B_N .
 \tag{33}
\]

Here is the positive overlap justification. The
[first-coordinate theorem, equation (26)](research_mixed_three_four_next_sectorwise_first_end.md)
bounds the sum of absolute values on the entire rectangle
\(a\ge A_N,\ 0\le b<N\) by \(CN^A e^{11N/6}\).
Every intersection of this rectangle with either second-index
deletion therefore has the same bound. The
[binomial end theorem, equations (16)--(17)](research_mixed_three_four_next_binomial_end_bound.md)
bounds the coherent first-coordinate sum on \(b\ge B_N\) by
rate \(9/5\), with normalized local jets of gap \(1/160\).
The low-index deletion is (24). Subtracting the positive
first-coordinate intersections, as in Section 3 of the low
physical interval theorem, does not require a modulus bound
on an arbitrary partial coherent prefix. The first-coordinate
terms and their intersections have normalized gap \(1/96\)
by equations (26)--(31) of their source theorem.

These fixed gaps are larger than \(\Delta/4\). Hence the complete
transfer of (31) satisfies (24), after harmless polynomial costs,
with the same smaller final allowance in (25). Apply the exact
subtraction (26) with \(E_N^{\rm all}\). This proves the corollary.
\(\square\)

This corollary concerns the \(11/12\) filter in (31). It does not
extend the argument to the later \(8/9\) filter, whose available
unit-disk correction rate is \(509/300\) rather than \(77/50\).
Nor does it bound the complementary source of the remaining
middle polynomial. The paired localization removes a correction
estimate from that assembly problem; the original middle
contribution still requires control.
