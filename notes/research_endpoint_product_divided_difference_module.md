# A divided-difference module for original endpoint products

Private written proof, 16 November 2026.

An exact six-channel divided-difference module for one original
endpoint kernel gives a fixed-dimensional module for every fixed
ordinary product. All source aliases are retained. A polynomial
change of channels gives a controlled-degree matrix equation whose
bounded-variable principal determinant has only the terminal and
microscopic factors. Its original-turn transport is literal.

The result is algebraic. It supplies neither a whole-source rate
nor a nonzero characteristic coefficient. In particular it does
not identify the rate of a turned product with the terminal rate.

## 1. Exact half-shift calculus and the original operator

Put
\[
 N\ge2,\quad q=e^{\pi i/N},\quad \kappa=q^{(N-1)^2/2},
 \quad s=q-q^{-1},\quad
 a=\frac{q+q^{-1}}2,\quad c_0=2a,\quad \zeta=q^2+q^{-2},
\]
\[
 z(v)=v+v^{-1},\quad z_\pm=z(q^{\pm1}v),\quad
 \delta=z_+-z_-=s(v-v^{-1}),\quad Z=z(v).
 \tag{1}
\]
For an ordinary spectral polynomial \(f\), define
\[
 \mathcal Df(Z)=\frac{f(z_+)-f(z_-)}{\delta},\qquad
 \mathcal Sf(Z)=\frac{f(z_+)+f(z_-)}2.
 \tag{2}
\]
Both expressions are ordinary polynomials in \(Z\). Indeed the
two spectral arguments have sum \(2aZ\) and product \(Z^2+s^2\);
the symmetric difference quotient has the same polynomial
property. These definitions also act on rational functions
where their denominators do not vanish.

Set
\[
 U_1=(a^2-1)Z,\qquad U_2=(a^2-1)(Z^2-4)=\delta^2/4.
\]
The exact identities are
\[
 \begin{split}
 \mathcal D(fg)&=(\mathcal Df)(\mathcal Sg)
                         +(\mathcal Sf)(\mathcal Dg),\\
 \mathcal S(fg)&=(\mathcal Sf)(\mathcal Sg)
                         +U_2(\mathcal Df)(\mathcal Dg),\\
 \mathcal D\mathcal S&=a\mathcal S\mathcal D+U_1\mathcal D^2,\\
 \mathcal S^2&=I+U_1\mathcal S\mathcal D+aU_2\mathcal D^2.
 \end{split}                                             \tag{3}
\]
The first two follow by expanding the two half shifts.
For a complete check of the last two, put
\(\delta_\pm=s(q^{\pm1}v-q^{\mp1}v^{-1})\). Then
\[
 \delta_+=a\delta+2U_1,\qquad
 \delta_-=a\delta-2U_1.                                  \tag{4}
\]
Compare the coefficients of \(f(z(q^2v))\) and
\(f(z(q^{-2}v))\) in the last two identities of (3).
For the third identity the needed coefficients are
\((a/2+U_1/\delta)/\delta_+=1/(2\delta)\) and
\((-a/2+U_1/\delta)/\delta_-=-1/(2\delta)\).
For the fourth they are
\((U_1/2+a\delta/4)/\delta_+=1/4\) and
\((-U_1/2+a\delta/4)/\delta_-=1/4\).
The middle coefficients then agree because the operators
annihilate constants in the third identity and preserve
constants in the fourth. This proves (3) as rational
identities, with their polynomial removable continuations.

Let \(\mathcal L\) be the original ordinary Askey--Wilson
operator from the pinned source. Define
\[
 \sigma(Z)=(2a^2-1)Z^2-4aZ+8-4a^2,\qquad
 \tau(Z)=2aZ-4.
 \tag{5}
\]
Then exactly
\[
                \mathcal L=c_0+s^2
                   \{\sigma\mathcal D^2+\tau\mathcal S\mathcal D\}.
 \tag{6}
\]
Here is a direct normalization check. The forward and backward
coefficients of \(\mathcal L-c_0\) are \(-A(v),-B(v)\), where
\[
 A(v)=-\frac{(qv-1)^4}{q(v^2-1)(q^2v^2-1)},\qquad
 B(v)=-\frac{(v-q)^4}{q(v^2-1)(v^2-q^2)}.
\]
The coefficients of \(\mathcal D^2,\mathcal S\mathcal D\)
are determined by
\[
 s^2\sigma=-\frac{\delta}{2}(A\delta_++B\delta_-),
 \qquad s^2\tau=-A\delta_++B\delta_-.
 \tag{7}
\]
Substitution gives (5). The middle coefficient follows by
applying both operators to \(1\). In particular
\[
 \sigma\longrightarrow(Z-2)^2,\qquad
 \tau\longrightarrow2(Z-2)
                 \quad\hbox{as }N\longrightarrow\infty.  \tag{8}
\]
No division by \(Z+2\) occurs in this presentation.

## 2. Six actual polynomial channels, with both source aliases

Retain the original kernel \(f_i(Z)=K_N(w_i,Z)\), and put
\[
 p(Z)=P_N(Z)=2T_N(Z/2)+2,\qquad
 \lambda_i=\frac{w_i-c_0}{s^2},\qquad
 \gamma_i=-\frac{P_N(w_i)}{N^4s^2},\qquad
 r_i(Z)=\frac{\gamma_i}{Z-c_0}.
 \tag{9}
\]
The original forcing is equivalent to the ordinary rational
identity
\[
 \sigma\mathcal D^2f_i+\tau\mathcal S\mathcal Df_i
                     -\lambda_i f_i=r_i p.              \tag{10}
\]
The product \(r_i p\) has its prescribed ordinary removable
continuation. The signs and powers of \(N\) follow from
\((w_i-\mathcal L)f_i=P_N(w_i)p/[N^4(Z-c_0)]\).

Since \(q^N=-1\), the aliases satisfy exactly
\[
                 \mathcal Dp=0,\qquad \mathcal Sp=4-p,
 \qquad \mathcal D1=0,\quad\mathcal S1=1.                 \tag{11}
\]
Thus the channel \(1\) must accompany \(p\). Applying a
half shift after prematurely setting \(p=0\) would lose (11).

Use the actual ordinary polynomial vector
\[
 Z_i=(f_i,d_i,h_i,t_i,p,1)^{\mathsf T},
 \quad d_i=\mathcal Df_i,\quad h_i=\mathcal Sf_i,\quad
 t_i=\mathcal S\mathcal Df_i.                             \tag{12}
\]
The following formulas explicitly construct rational matrices
\(\mathbf D_i,\mathbf S_i\) with
\(\mathcal DZ_i=\mathbf D_i Z_i\),
\(\mathcal SZ_i=\mathbf S_i Z_i\).
All scalar operations \(\mathcal D,\mathcal S\) on coefficients
below have the definition (2).

Write \(X_i=\mathcal D^2f_i\), \(Y_i=\mathcal D^3f_i\),
\(Z_i^{(2)}=\mathcal S\mathcal D^2f_i\), and define
\[
 X_i=\frac{\lambda_i f_i-\tau t_i+r_i p}{\sigma},
\]
\[
 A=\mathcal S\sigma+U_1\mathcal S\tau+aU_2\mathcal D\tau,
 \qquad
 B=\mathcal D\sigma+a\mathcal S\tau+U_1\mathcal D\tau,
\]
\[
 u_i=(\mathcal Dr_i)(4-p)+(\lambda_i-\mathcal D\tau)d_i,
 \qquad
 v_i=(\mathcal Sr_i)(4-p)-(\mathcal S\tau)d_i+\lambda_i h_i.
 \tag{13}
\]
Applying \(\mathcal D\) and \(\mathcal S\) to (10), with (3),
gives exactly
\[
 \begin{pmatrix}A&B\\ U_2B&A\end{pmatrix}
       \binom{Y_i}{Z_i^{(2)}}=\binom{u_i}{v_i}.            \tag{14}
\]
For example the coefficient of \(\mathcal D^3f_i\) in the
first row is
\(\mathcal S\sigma+U_1\mathcal S\tau+aU_2\mathcal D\tau\);
in the second it is \(U_2B\). The remaining lower terms
are precisely the two terms in \(d_i,h_i\) displayed in (13).

This determinant has an exact factorization. Put
\(b=2a^2-1=\zeta/2\). Directly from (5),
\[
 A=(2b^2-1)Z^2-4bZ+8-4b^2,\qquad
 B=4a(bZ-2),
\]
\[
 \Delta:=A^2-U_2B^2=(Z-2b)^4=(Z-\zeta)^4.
 \tag{15}
\]
To check the last equality, substitute
\(U_2B^2=4(b^2-1)(Z^2-4)(bZ-2)^2\) and expand; the
coefficients are \(1,-8b,24b^2,-32b^3,16b^4\).
In particular \(\Delta\) is never the zero polynomial.
The explicit solution of (14) is
\[
 Y_i=(Au_i-Bv_i)/\Delta,\qquad
 Z_i^{(2)}=(-U_2Bu_i+Av_i)/\Delta.                        \tag{16}
\]
The matrices are now completely specified by the six rows
\[
 \mathcal DZ_i=
 (d_i,\ X_i,\ at_i+U_1X_i,\ aZ_i^{(2)}+U_1Y_i,\ 0,\ 0)^{\mathsf T},
\]
\[
 \mathcal SZ_i=
 (h_i,\ t_i,\ f_i+U_1t_i+aU_2X_i,\
       d_i+U_1Z_i^{(2)}+aU_2Y_i,\ 4-p,\ 1)^{\mathsf T}.
 \tag{17}
\]
Each entry on the right is the indicated linear form in (12).

Here is an explicit common denominator:
\[
 d_0(Z)=\sigma(Z)(Z-c_0)(Z-2)(Z-\zeta)^5.                 \tag{18}
\]
Indeed
\[
 (z_+-c_0)(z_--c_0)=(Z-2)(Z-\zeta),
\]
\[
 \mathcal Dr_i=-\frac{\gamma_i}{(Z-2)(Z-\zeta)},\qquad
 \mathcal Sr_i=\frac{\gamma_i(aZ-c_0)}
                         {(Z-2)(Z-\zeta)}.              \tag{19}
\]
Equations (13)--(17) prove the denominator assertion.
For \(N\ge5\), \(d_0\) has degree \(9\), and
\[
                         d_0(Z)\longrightarrow(Z-2)^9.
 \tag{20}
\]
The rational module itself is valid for every \(N\ge2\);
the degree and principal statements below use \(N\ge5\).
All denominators mean rational identities first, followed
by clearing; they are not inverted in the physical quotient.

## 3. Exact ordinary products and a polynomial channel gauge

Fix \(r\ge1\). Tensor the six-channel vectors:
\[
 \mathcal Z=Z_1\otimes\cdots\otimes Z_r,\qquad d_r=6^r.
 \tag{21}
\]
Its first component is the actual ordinary product
\(\prod_i K_N(w_i,Z)\). For a subset \(I\) of the \(r\)
indices let \(T_I\) be the ordered tensor of \(\mathbf D_i\)
at indices in \(I\) and \(\mathbf S_i\) at the others.
The product rules give the explicit matrices
\[
 \mathbf D=\sum_{|I|\ {\rm odd}}U_2^{(|I|-1)/2}T_I,\qquad
 \mathbf S=\sum_{|I|\ {\rm even}}U_2^{|I|/2}T_I,
\]
\[
                 \mathcal D\mathcal Z=\mathbf D\mathcal Z,
 \qquad          \mathcal S\mathcal Z=\mathbf S\mathcal Z.
 \tag{22}
\]
One proof expands each half-shift as
\(\mathcal S\pm(\delta/2)\mathcal D\) before multiplying;
the even and odd terms give (22). In particular this is
ordinary multiplication, not multiplication transported by
the physical turn.

A degree gauge is useful before converting back to \(J\).
Give the six channels in (12) the weights
\[
                             (0,-1,0,-1,1,1).            \tag{23}
\]
Weights here describe rational coefficient degrees at
infinity; they are not the actual degrees of \(p\) or \(f_i\).
Inspection of (13)--(17) gives
\[
 \deg_\infty(\mathbf D_i)_{ab}\le w_a-w_b-1,\qquad
 \deg_\infty(\mathbf S_i)_{ab}\le w_a-w_b.                \tag{24}
\]
For completeness, \(X_i\) has weighted degree \(-2\);
the right sides \(u_i,v_i\) have weighted degrees \(-1,0\);
since \(\deg A\le2,\deg B\le1,\deg\Delta=4\), (16) gives
weighted degrees \(-3,-2\) for \(Y_i,Z_i^{(2)}\).
These bounds prove every row of (24), using
\(\deg U_1=1,\deg U_2=2\).
They hold for \(N\ge5\); vanishing scalar coefficients do
not worsen them.

For tensor channels, add the weights, writing \(w_a\in[-r,r]\).
Each term of (22) then has the same bounds (24): its powers
of \(U_2\) exactly compensate all but one of the degree
losses from the odd number of \(\mathbf D_i\), or all of
them in the even case.

Put
\[
 a_a=r-w_a\in\{0,\ldots,2r\},\qquad
 P(Z)=\operatorname{diag}((Z-2)^{a_a}),\qquad
 \mathcal W=P\mathcal Z.
 \tag{25}
\]
This is a polynomial change of actual channels, not an
inverse in the quotient. Its exact rational matrices are
\[
 \widetilde{\mathbf D}
  =\{(\mathcal SP)\mathbf D+(\mathcal DP)\mathbf S\}P^{-1},
\]
\[
 \widetilde{\mathbf S}
  =\{(\mathcal SP)\mathbf S+U_2(\mathcal DP)\mathbf D\}P^{-1}.
 \tag{26}
\]
Here \(P^{-1}\) is used only in the rational calculation.
The entrywise degree bounds become
\[
 \deg_\infty\widetilde{\mathbf D}_{ab}\le-1,\qquad
 \deg_\infty\widetilde{\mathbf S}_{ab}\le0.
 \tag{27}
\]
For example the first term in the first formula has degree
at most \(a_a+w_a-w_b-1-a_b=-1\); the other three
terms are checked the same way.
A common denominator for both matrices is
\[
                         e(Z)=d_0(Z)^r(Z-2)^{2r}.
 \tag{28}
\]
It has degree \(11r\), with limit \((Z-2)^{11r}\).
Thus their numerators can be taken of degrees at most
\(11r-1\) and \(11r\), respectively.

## 4. A controlled-degree \(C,J\) matrix and its principal determinant

For a polynomial \(g\), define its half-shift norm
\[
             \mathcal N_qg(Z)=g(z_+)g(z_-).
 \tag{29}
\]
It is polynomial. If \(g\) has degree \(k\) and leading
coefficient \(g_k\ne0\), its degree is \(2k\), with
leading coefficient \(g_k^2\). This follows from
\(z_+z_-=Z^2+s^2\). For a rational function \(f/g\),
both \(\mathcal S(f/g)\) and \(\mathcal D(f/g)\) have
denominator \(\mathcal N_qg\): their numerators are the
symmetric sum and divided antisymmetric difference of
\(f(z_+)g(z_-)\) and \(f(z_-)g(z_+)\).
Their numerator degrees are at most
\(\deg f+\deg g\) and \(\deg f+\deg g-1\), respectively.

Apply \(\mathcal D,\mathcal S\) entrywise to matrix
coefficients. Equations (3),(6),(26) give exactly
\[
 \mathcal L\mathcal W=c_0\mathcal W+s^2\mathbf H(Z)\mathcal W,
\]
\[
 \begin{split}
 \mathbf H={}&\sigma\{(\mathcal S\widetilde{\mathbf D})
                         \widetilde{\mathbf D}
                   +(\mathcal D\widetilde{\mathbf D})
                         \widetilde{\mathbf S}\}\\
 &+\tau\{(\mathcal S\widetilde{\mathbf D})
                         \widetilde{\mathbf S}
                   +U_2(\mathcal D\widetilde{\mathbf D})
                         \widetilde{\mathbf D}\}.
 \end{split}                                             \tag{30}
\]
Matrix multiplication order in this formula is literal.
Define
\[
 d(Z)=e(Z)\mathcal N_qe(Z),\qquad
 E(Z)=d(Z)\mathbf H(Z).
 \tag{31}
\]
These are a scalar polynomial and a polynomial matrix,
and the exact degree bounds are
\[
                         \deg d=33r,\qquad
                         \deg E_{ab}\le33r.              \tag{32}
\]
Indeed write \(l=11r\). The numerators of
\(\mathcal S\widetilde{\mathbf D}\) and
\(\mathcal D\widetilde{\mathbf D}\) have degrees at most
\(2l-1,2l-2\) over \(\mathcal N_qe\).
Combining with (27), and then the degrees \(2,1,2\)
of \(\sigma,\tau,U_2\), bounds every numerator in (30)
by \(3l=33r\).

Every entry of \(\mathcal W\) is an ordinary polynomial.
Clearing (30) therefore gives an ordinary polynomial
identity, and then the exact full-algebra relation
\[
 \boxed{\quad
       \{d(C)(J-c_0)I-s^2E(C)\}\,
                          \operatorname{can}\mathcal W=0.
 \quad}                                                   \tag{33}
\]
Canonical reduction is componentwise. Neither \(d(C)\)
nor \(P(C)\) is inverted.

Now assume \(w_i=2\cosh(\alpha_i/N)\), with all \(\alpha_i\)
in fixed bounded complex sets. Then \(\lambda_i\) is
bounded and has a limit, and \(\gamma_i=O(N^{-2})\).
All rational matrix coefficients above have bounded limits
on compact sets avoiding \(Z=2\). Entrywise half-shift
divided differences of fixed-degree coefficient polynomials
converge to their derivatives, so they introduce no
uncontrolled \(s^{-1}\) coefficient. The cleared polynomial
coefficients in \(E\) remain bounded as well. Moreover
\[
                         d(Z)\longrightarrow(Z-2)^{33r}.
 \tag{34}
\]
Thus the commuting, bounded-variable principal matrix of
(33) is precisely
\[
                         (X-2)^{33r}(Y-2)I_{6^r},
\]
and its determinant is
\[
                    (X-2)^{33r\,6^r}(Y-2)^{6^r}.         \tag{35}
\]
This is a characteristic containment statement for the
specified matrix presentation. It is not a claim that the
minimal scalar characteristic has these exact multiplicities
or that every displayed component participates.
In particular it establishes no separate \(X=-2\) factor
in this controlled presentation; no such factor was
discarded by an assumption about the solution.

## 5. Original turns, recovery, and the physical leading order

Retain \(V_n=\kappa^nTR^{-n}T\), \(D_n=V_nCV_{-n}\) and
\(V_nJ=JV_n\). Applying the original turn componentwise
to (33) gives exactly
\[
 \boxed{\quad
 \{d(D_n)(J-c_0)I-s^2E(D_n)\}\,\mathcal F=0,\qquad
 \mathcal F=V_n\operatorname{can}\mathcal W .
 \quad}                                                   \tag{36}
\]
Every original ungauged channel is retained by the forced
recovery equations
\[
 (D_n-2)^{a_a}\,\mathcal Y_a=\mathcal F_a,\qquad
 \mathcal Y_a=V_n\operatorname{can}\mathcal Z_a.
 \tag{37}
\]
In particular the turned original product is the first
component of \(\mathcal Y\), whose recovery exponent is
\(r\). Equation (37) is never solved by dividing by
\(D_n-2\). Its actual homogeneous directions and anchors
are part of the original source.

Let \(x_n,y\) be the physical commuting symbols of
\(D_n,J\) in the pinned operator/transfer convention.
The principal determinant of (36) is
\[
                      (x_n-2)^{33r\,6^r}(y-2)^{6^r}.
 \tag{38}
\]
Recovery adds only factors \(x_n-2\).
There is also a useful exact leading-order fact, beyond
merely taking this determinant. For fixed \(n\ne0\), put
\(m=|n|\), \(k=33r\). The physical difference order of the
first term \(d(D_n)J\) is \(km+1\) in each direction.
Its two extreme coefficients are scalar multiples of
the identity matrix and are nonzero on every buffered
compact physical interval for all sufficiently large \(N\).
This follows from the exact two extreme coefficients of
\(D_n\), their shifted products, and the nonzero extreme
coefficients of \(J\) in the bulk-transfer source.
The leading coefficient of \(d\) tends to \(1\).
All other terms in (36) have physical shift order at most
\(km\), by (32). Hence the \(s^2E(D_n)\) correction cannot
create a new highest-order recurrence coefficient.
On a compact physical interval the normalized block-companion
coefficients converge to the scalar leading matrix times the
channel identity, whose determinant is (38).
For \(n=0\), the separate equation has the usual first
physical shift order of \(J\), with coefficient \(d(C)\),
which is a unit on such an interval for large \(N\).

This leading-order statement still supplies no transfer
estimate. The multiple roots, the coupled channels, the
forced recovery, and all actual initial directions remain
to be estimated. Even a compact transfer upper bound would
not by itself make the initial channels polynomially small
after turning. No equality with a terminal growth budget
is asserted here.

Both (33) and (36)--(37) hold in the original
\(\mathbb C[Z]/(P_N)\), so all double-root first normals,
the odd simple values, shared spectators and original
crossing phases remain. More explicitly, their ordinary
polynomial residuals are \(P_N\) multiples.
In the physical scaled coordinate
\(c_N(u)=2\cos(2\pi u+\pi/N)\), one has
\(P_N(c_N(u))=4\sin^2(\pi Nu)\). Therefore the value and
first \(u\)-derivative equations hold exactly at every
regular physical row. Differentiating them includes every
coefficient derivative and gives the original normal
system; it does not differentiate a quotient identity
off the physical grid.

The operations \(\mathcal D,\mathcal S\) themselves were
applied to the ordinary polynomials before canonical
reduction. They need not preserve the ideal \((P_N)\),
as (11) already shows. Ordinary outside parameters are
never quotiented, and their fixed mixed derivatives can
be retained throughout the explicit matrix identities.

## 6. Direct sources and scope

Both complete direct sources were read at their matching
hashes, with their directly used implications checked:

* [Original operator and branching source](research_unit_turn_finite_band_branching_operator.md),
  SHA256 31d9f574c7dc3aaac07e4eb50c131b3328be46b3c2a2ef46f9dae7f0c4ddb9cb:
  exact ordinary AW equation, source normalization, ideal
  preservation, and ordered original-turn conjugation.
* [Exact physical terminal operator](research_terminal_twist_bulk_transfer_bound.md),
  SHA256 fca96865315f21dc9961be89061cc6c3a292b2b563e7ded756e86c3438ef5bde:
  physical shift convention, extreme coefficients and
  ordinary-residual justification of full normal equations.

The six-channel closure, polynomial tensor gauge, denominator
list and controlled degree are proved above. The earlier
source-retaining tensor annihilator supplies complementary
generic elimination; it is not used to infer (35) or (38).
The gauge was checked independently in collaboration with
the coefficient reviewer. No product-rate or arbitrary
short-component theorem is claimed.

Only written mathematics and source-text/hash reads were
used. No mathematical program, numerical experiment, test
or build was run. Adopted notes and public manuscripts are
unchanged.
