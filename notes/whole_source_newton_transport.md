# Whole-source Newton transport and the finite-root normal lattice

This note proves a boundary quantum-torus calculation, retaining the whole
meridian variable and its normal directions. It does **not** yet assert that an
arbitrary marked crossing or bridge recoupling has been realized by these
operators. In particular, it does not prove the remaining triple-to-cyclotomic
transform in [the \(5_2\) source reduction](five_two_whole_source_reduction.md).

No literature proof is used. Comparisons with torus skeins or rank-one
Askey--Wilson algebras supply background terminology only.

The [independent lattice/cut audit](source_lattice_independent_audit.md)
gives a second ring proof and checks the physical derivative convention.

## 1. A source basis and three banded operators

Initially let \(Q\) be an indeterminate and work in \(k[Y,Y^{-1}]\), where
\(k=\mathbb Q(Q)\). Set

\[
 X=Y+Y^{-1},\qquad
 t_n(Y)=\prod_{r=1}^n(X-Q^r-Q^{-r}),\qquad
 v_n(Y)=(1-Y)t_n(Y).
\]

The lower-case \(t_n\) is a Newton polynomial. The upper-case \(T\) denotes
the shift

\[
 (Tf)(Y)=f(QY),\qquad TY=QYT.
\]

The following product fixes every factor and power:

\[
 v_n(Y)=-Y^{n+1}(Q^{-n}/Y;Q)_{2n+1}.                 \tag{1.1}
\]

Define

\[
 S=T+QT^{-1},\qquad Z=YT+QY^{-1}T^{-1},
\]

and

\[
 a_n=Q^n+Q^{-n},\quad
 \gamma_n=Q^{n+1}+Q^{-n},\quad
 \delta_n=Q^{-2n}(1-Q^{2n})(1-Q^{2n+1}).
\]

With \(v_{-1}=0\), the exact Laurent-polynomial identities are

\[
 \boxed{Xv_n=v_{n+1}+a_{n+1}v_n,}                  \tag{1.2}
\]

\[
 \boxed{Sv_n=\gamma_n v_n+\delta_n v_{n-1},}        \tag{1.3}
\]

\[
 \boxed{Zv_n=Q^{n+1}v_{n+1}
 +(1+Q)Q^{2n+1}v_n+Q^n\delta_n v_{n-1}.}           \tag{1.4}
\]

These hold over \(\mathbb Z[Q,Q^{-1}]\). They therefore specialize at every
nonzero \(Q\), including \(Q=-1\), without a \(1-Q^2\) denominator.

### Proof

The first identity is the defining Newton recurrence. Let

\[
 (Jf)(Y)=-Yf(Y^{-1}).
\]

Then \(J^2=1\), \(Jv_n=v_n\), and

\[
 JTJ=QT^{-1},\qquad JYJ=Y^{-1}.
\]

Thus \(S,Z\) preserve the \(J\)-fixed Laurent polynomials. These are exactly
\((1-Y)k[X]\): evaluation at \(Y=1\) gives divisibility by \(1-Y\), and after
division the quotient is invariant under \(Y\leftrightarrow Y^{-1}\).

For generic \(Q\), (1.1) shows that \(Sv_n\) is divisible by \(v_{n-1}\).
The quotient is invariant under inversion and has Laurent degree at most one,
so it is affine in \(X\). Comparing the top coefficient
\(v_n=-Y^{n+1}+\cdots\) gives the coefficient \(\gamma_n\) of \(v_n\).
Evaluation at \(Y=Q^n\) then gives

\[
 \delta_n
 =\frac{v_n(Q^{n+1})}{v_{n-1}(Q^n)}
 =Q^{2n+1}(1-Q^{-2n})(1-Q^{-2n-1})
 =Q^{-2n}(1-Q^{2n})(1-Q^{2n+1}).
\]

For \(n=0\), (1.3) is directly \(S(1-Y)=(1+Q)(1-Y)\).
This proves (1.3) generically and hence as an integral Laurent identity.
Finally,

\[
 (1-Q^2)Z=XS-QSX.                                 \tag{1.5}
\]

Substituting (1.2)--(1.3) and cancelling this polynomial factor before
specialization gives (1.4). It does not divide by \(1-Q^2\) after setting
\(Q=-1\).

## 2. The exact finite-root corner

Let \(Q\) now be a primitive \(N\)-th root, \(N\ge2\), in a characteristic-zero
field \(k\). Introduce

\[
 A=k[U,U^{-1}],\qquad
 B=A[Y]/(Y^N-U)=k[Y,Y^{-1}].                        \tag{2.1}
\]

The last equality specifies the \(A\)-algebra structure \(U=Y^N\).
The power basis is \(1,Y,\ldots,Y^{N-1}\). The shift \(T\) is \(A\)-linear
and \(T^N=1\). Put

\[
 W=U+U^{-1}-2=\frac{(U-1)^2}{U}.
\]

There is the exact product identity

\[
 t_N=W,\qquad t_{n+N}=Wt_n,\qquad v_{n+N}=Wv_n.     \tag{2.2}
\]

Indeed

\[
 Y^Nt_N(Y)=\prod_{r=1}^N(Y-Q^r)(Y-Q^{-r})
          =(Y^N-1)^2,
\]

and the factors repeat with period \(N\). Define

\[
 L=\bigoplus_{n=0}^{N-1}A v_n\subset B.             \tag{2.3}
\]

Independence is proved in section 3. Equations (1.2)--(1.4), with
\(v_N=Wv_0\), give banded \(N\times N\) matrices on this whole-source
lattice. In column convention, the columns \(0\le n<N-1\) are exactly
(1.2)--(1.4), while the last columns are

\[
 Xv_{N-1}=Wv_0+2v_{N-1},                           \tag{2.4}
\]

\[
 Sv_{N-1}=\gamma_{N-1}v_{N-1}
                +\delta_{N-1}v_{N-2},              \tag{2.5}
\]

\[
 Zv_{N-1}=Wv_0+(1+Q)Q^{-1}v_{N-1}
                +Q^{-1}\delta_{N-1}v_{N-2}.        \tag{2.6}
\]

At \(n=0\), the lower term is zero since \(\delta_0=0\). For \(N=2\),
contributions in the same row are added.

The corner \(Wv_0\) is retained. It vanishes to order two at \(U=1\),
rather than being identically zero; deleting it changes second and higher
normal jets.

## 3. The normal lattice and its saturation

The involution \(J\) acts on \(B=k[Y,Y^{-1}]\), but is **semilinear** over \(A\):

\[
 J(a(U)f)=a(U^{-1})Jf.                             \tag{3.1}
\]

It becomes \(A\)-linear modulo \(U^2-1\). There is the exact characterization

\[
 \boxed{L=\{f\in B:Jf-f\in(U^2-1)B\}.}             \tag{3.2}
\]

In particular,

\[
 \boxed{(U^2-1)B\subset L\subset B.}                \tag{3.3}
\]

Since the Newton polynomials are monic, this \(A\)-span is independent of
the choice of primitive \(Q\):

\[
 L=(1-Y)\operatorname{span}_A\{1,X,\ldots,X^{N-1}\}. \tag{3.4}
\]

### Proof of (3.2)--(3.3)

Every \(J\)-fixed Laurent polynomial is \((1-Y)\) times a polynomial in
\(X\). Expand in the monic Newton basis and fold using (2.2); it belongs
to \(L\). The inclusion from left to right in (3.2) follows from (3.1)
and \(a(U^{-1})-a(U)\in(U^2-1)A\).

For any \(h\in B\), use its \(k\)-linear \(J\)-eigenspace decomposition
\(h=h_++h_-\). We have \(h_+\in L\), and

\[
 J\big((U-U^{-1})h_-\big)=(U-U^{-1})h_-.
\]

Thus \((U-U^{-1})h_-\in L\); multiplication by the unit \(U\) shows
\((U^2-1)h_-\in L\). This proves (3.3). If \(Jf-f\in(U^2-1)B\), then
\(f_-=(f-Jf)/2\in(U^2-1)B\subset L\), and \(f_+\in L\). This proves (3.2).

### Independence and determinant

Over an algebraic closure of \(k(U)\), write \(y_j=Q^j y\), \(y^N=U\), and
\(x_j=y_j+y_j^{-1}\). The \(x_j\) are distinct away from \(U^2=1\):
equality for distinct \(i,j\) would force \(y_i y_j=1\), hence \(U^2=1\).
Also \(1-y_j\ne0\) away from \(U=1\). The monic Newton evaluation matrix
multiplied by \(\operatorname{diag}(1-y_j)\) is therefore invertible
generically. This proves independence over \(A\) and spanning over \(k(U)\).

Let \(M_N\) be the coefficient matrix of \(v_0,\ldots,v_{N-1}\) in
\(1,Y,\ldots,Y^{N-1}\), with increasing columns. Then

\[
 \begin{aligned}
 \det M_N
 &=\prod_j(1-y_j)\prod_{i<j}\frac{x_j-x_i}{y_j-y_i}\\
 &=(1-U)\prod_{i<j}(1-(y_i y_j)^{-1})\\
 &=\boxed{\begin{cases}
 (1-U)(1-U^{-2})^{(N-1)/2},&N\text{ odd},\\
 -U(1-U^{-2})^{N/2},&N\text{ even}.
 \end{cases}}                                    \tag{3.5}
 \end{aligned}
\]

For odd \(N\), each residue \(i+j\pmod N\) occurs \((N-1)/2\) times among
unordered distinct pairs. For \(N=2m\), even residues occur \(m-1\) times
and odd residues \(m\) times. Their products are \(1-U^{-1}\) and
\(1+U^{-1}\), respectively, giving the displayed even sign.

The Smith factors over the PID \(A\), up to units, are

\[
 \begin{array}{c|c}
 N=2m&1\ (m\text{ times}),\quad U^2-1\ (m\text{ times}),\\
 N=2m+1&1\ (m\text{ times}),\quad U-1,\quad
                    U^2-1\ (m\text{ times}).
 \end{array}                                     \tag{3.6}
\]

To see the multiplicities, reduce (3.2) at \(U=\pm1\), where \(J\) is an
ordinary involution. Evaluation on reciprocal pairs of roots gives

\[
 \dim\operatorname{im}(L\longrightarrow B/(U-1)B)
 =\begin{cases}(N-1)/2,&N\text{ odd},\\N/2,&N\text{ even}.\end{cases} \tag{3.7}
\]

At \(Y=1\), a fixed function must vanish; at \(Y=-1\), there is no
condition. At \(U=-1\), the rank is \((N+1)/2\) for odd \(N\), and \(N/2\)
for even \(N\). Inclusion (3.3), or these ranks together with (3.5), shows
that all nontrivial local Smith exponents are one.

Crucially, \(L/(U-1)L\) has dimension \(N\), whereas its image in
\(B/(U-1)B\) has only the dimension in (3.7). The lost directions are
retained by first normal jets of the embedding \(L\subset B\).

For another description, let \(C_n(Y+Y^{-1})=Y^n+Y^{-n}\). On the abstract
fiber \(L/(U-1)L\), both the characteristic and minimal polynomials of
the \(X\) matrix equal \(C_N(x)-2\). Indeed \(v_0\) is a cyclic vector by
the Newton recurrence. The repeated roots give size-two Jordan blocks.
On \(B/(U-1)B\), multiplication by \(X\) is diagonalizable by evaluation
at the distinct \(N\)-th roots. The two fibers must not be identified.

## 4. Cleared recovery of the clock and shift

Define integer polynomials by

\[
 C_0(x)=2,\quad C_1(x)=x,\quad C_{n+1}(x)=xC_n(x)-C_{n-1}(x),
\]

\[
 P_{-1}(x)=0,\quad P_0(x)=1,\quad
 P_{n+1}(x)=xP_n(x)-P_{n-1}(x).
\]

Thus \(P_j(x)=\mathcal U_j(x/2)\), and

\[
 P_{N-1}(X)(Y-Y^{-1})=U-U^{-1},\qquad
 P_{N-1}(X)Y^{-1}=P_{N-2}(X)+U^{-1}.               \tag{4.1}
\]

Write \(D=U-U^{-1}\). On the original regular power lattice \(B\), the
following are exact cleared operator identities:

\[
 \boxed{DY=C_{N+1}(X)-U^{-1}X,}                    \tag{4.2}
\]

\[
 \boxed{DY^{-1}=C_{N-1}(X)-U^{-1}X,}               \tag{4.3}
\]

\[
 \boxed{DT=P_{N-1}(X)Z
              -(P_{N-2}(X)+U^{-1})S,}             \tag{4.4}
\]

\[
 \boxed{QD T^{-1}=(P_{N-2}(X)+U)S-P_{N-1}(X)Z.}   \tag{4.5}
\]

For (4.2), expand \(C_{N+1}(X)=UY+U^{-1}Y^{-1}\); (4.3) is analogous.
For (4.4), use \(Z-Y^{-1}S=(Y-Y^{-1})T\) and (4.1).
Subtracting (4.4) from \(DS\) gives (4.5). Operator order is as displayed;
the polynomials in \(X\) multiply on the left.

Thus \(X,S,Z\) recover the full quantum-torus action over \(k(U)\), and
recover its cleared equations over \(A\). Dividing by \(D\) and then
substituting \(U=1\) is not a recovery rule. Use the regular action on \(B\),
or retain the compatible lattice and normal jets, before specialization.

There is a uniform denominator bound. For any \(A\)-linear endomorphism
\(R\) of \(B\),

\[
 DR(L)\subset L,                                  \tag{4.6}
\]

since \(R(L)\subset B\) and \(DB=(U^2-1)B\) up to a unit. Its matrix in
the \(v_n\) basis therefore has at most a simple pole at each of
\(U=1,-1\), independently of its clock/shift word length. Higher poles
appearing in products of (4.2)--(4.5) cancel. This applies to an operator
already proved regular and \(A\)-linear on \(B\); it supplies neither
hypothesis for an uncomputed crossing.

For reference, clock and shift generate all \(A\)-linear endomorphisms of
\(B\). The projectors

\[
 E_j=\frac1N\sum_{\ell=0}^{N-1}Q^{-j\ell}T^\ell
\]

project onto \(AY^j\), and \(Y^{i-j}E_j\) are matrix units.

## 5. Reciprocal sources and the marked cut

If an actual marked source calculation gives a reciprocal Laurent polynomial
\(F(Y)=F(Y^{-1})\), then

\[
 f(Y)=(1-Y)F(Y)\in L.                             \tag{5.1}
\]

This follows from whole reciprocity, rather than ordinary-color
interpolation. For a finite Newton expansion \(F=\sum_n c_n t_n\), every
tail folds exactly:

\[
 f=\sum_{r=0}^{N-1}
       \left(\sum_{a\ge0}c_{r+aN}W^a\right)v_r.    \tag{5.2}
\]

Terms with index \(r+aN\) start at normal order \(2a\) at \(U=1\); vanishing
at the point does not discard them as whole functions.

Define the marked cut on \(L\subset k[Y,Y^{-1}]\) by

\[
 \operatorname{cut}(f)=-\left.\frac{df}{dY}\right|_{Y=1}.             \tag{5.3}
\]

This derivative follows \(U=Y^N\). It is **not** the derivative at fixed
\(U\) of a chosen power-basis representative. Every \(f\in L\) vanishes
at \(Y=1\), so

\[
 \operatorname{cut}((U-1)f)=0,\qquad
 \operatorname{cut}(v_n)=t_n(1)
       =\prod_{r=1}^n(2-Q^r-Q^{-r}).               \tag{5.4}
\]

Thus cut factors through the full abstract fiber \(L/(U-1)L\).
If \(f=\sum_{n<N}b_n(U)v_n\), then

\[
 \boxed{F(1)=\operatorname{cut}(f)
       =\sum_{n=0}^{N-1}b_n(1)
          \prod_{r=1}^n(2-Q^r-Q^{-r}).}            \tag{5.5}
\]

Cut need not factor through the image in \(B/(U-1)B\). For \(N=3\),
\(Q+Q^{-1}=-1\), and

\[
 v_1=(1-Y)(Y+Y^{-1}+1)=\frac{1-U}{Y}.
\]

Its image in \(B/(U-1)B\) is zero, but its cut is \(3\). This is an exact
example of the normal data required by the selected period.

More generally, \(v_{\lfloor N/2\rfloor}\) has zero image in that power
fiber: the factors \(t_{\lfloor N/2\rfloor}\) cover every nontrivial
reciprocal pair of roots, and \(1-Y\) kills \(Y=1\). Its cut is nonzero,
and is positive at the principal complex root. Thus this phenomenon
already occurs among exactly \(J\)-fixed whole sources at every level.

Equations (5.1)--(5.5) do not determine uncomputed Newton coefficients.
For the actual figure-eight source proved in
[the figure-eight source identity](figure_eight_whole_source_identity.md), the coefficients are
\(b_n=1\). For the actual \(5_2\) triple sum, the proposed coefficient
transform remains unproved.

## 6. A whole annihilator can be put in the banded algebra

This section is conditional on an actual source annihilator, not on a
conjectured recurrence or its geometric interpretation.
Let \(\mathcal Q=k\langle Y^{\pm1},T^{\pm1}\rangle/(TY-QYT)\).
Conjugation by \(J\) induces the involution

\[
 \theta(Y)=Y^{-1},\qquad\theta(T)=QT^{-1}.
\]

Its fixed algebra is exactly the algebra generated by \(X,S,Z\).
Here is an elementary proof. Its fixed vector space is spanned by \(1\)
and the orbit sums

\[
 E_{a,b}=Y^aT^b+Q^bY^{-a}T^{-b}.
\]

They obey

\[
 XE_{a,b}=E_{a+1,b}+E_{a-1,b},\qquad
 E_{a,b}S=E_{a,b+1}+QE_{a,b-1},
\]

\[
 E_{1,-1}=Q^{-1}(XS-Z),\qquad
 E_{-a,b}=Q^bE_{a,-b}.
\]

Starting from \(E_{0,0}=2\), \(E_{1,0}=X\), \(E_{0,1}=S\),
\(E_{1,1}=Z\), these recurrences generate every orbit sum.
The proof works before or after root specialization in characteristic zero.

At \(Q=1\), the commuting symbols obey
\(x^2+s^2+z^2-xsz-4=0\), as direct substitution of
\(x=Y+Y^{-1}\), \(s=T+T^{-1}\), \(z=YT+Y^{-1}T^{-1}\) shows.
This identifies the classical fixed algebra with the Weyl quotient of
the boundary torus; it does not choose a longitude convention for \(T\).

Suppose \(F\) is reciprocal and an actual nonzero quantum-torus operator
\(P\) annihilates it. For \(f=(1-Y)F\), conjugate to
\((1-Y)P(1-Y)^{-1}\) in the rational-coefficient shift algebra and clear its
finitely many \(Y\)-denominators by left multiplication. This gives a
nonzero Laurent operator \(R\in\mathcal Q\) with \(Rf=0\).
Since \(Jf=f\), also \(\theta(R)f=0\).

If \(R+\theta(R)\ne0\), this is a nonzero invariant annihilator. Otherwise
\(R\) is anti-invariant and

\[
 (Y-Y^{-1})R
\]

is a nonzero invariant annihilator. Nonzeroness uses the fact that the
abstract quantum torus is a domain, also at roots of unity; no quotient
by \(T^N-1\) is taken in this domain assertion. By the fixed-algebra result,
the resulting annihilator is a noncommutative polynomial in \(X,S,Z\).
It therefore acts by a finite-band expression in the whole source basis,
with the exact corner in section 2.

This proves an operator-existence statement whenever the actual annihilator
and reciprocity have been established. It does not select a particular
operator, prove that its classical symbol is the geometric \(A\)-component,
or prove a regulator/volume statement.

For the actual reduced knot family these hypotheses have already been
established in the repository: [actual Weyl descent, section 1](actual_weyl_descent.md)
proves reciprocity at every level for every knot, and
[squared-meridian descent, section 2](even_meridian_norm_descent.md), using
[the finite-sum proof](finite_sum_annihilator.md), supplies a nonzero
all-level annihilator over \(\mathbb Q(Q,Y)\). Clearing its finitely many
denominators gives the Laurent input used here. The argument applies
levelwise to \(f_N=(1-Y)F_N\) with this same operator and therefore gives
a nonzero all-level annihilator in the algebra generated by \(X,S,Z\).
This corollary has no hyperbolicity, alternatingness, or bridge-number
restriction. It remains an existence statement, without a selected
geometric symbol or a volume estimate.

## 7. Reproducible checks

[The audit script](../experiments/audit_whole_source_newton_transport.py) independently checks
the integral Laurent identities, exact finite-root matrix intertwining,
determinants and fiber ranks, and cleared clock/shift recovery.
The saved JSON reports checks; proofs are supplied above.
The completed audit passes 78 generic integral Laurent identities,
148 orbit-sum identities, and 108 exact finite-root checks at
\(N=2,\ldots,10\), including the un-specialized \(U\) corners.

The subsequent [actual Newton transform](newton_actual_source_canonical_transform.md)
constructs generic coefficients and their recurrence from actual fixed
colors, proves quantum birationality, and retains the selected whole
parameter-germ period. The [source/monodromy chain map](source_lattice_monodromy_chainmap.md)
also transports its scalar source and physical normal cut. The
[geometric resolution](newton_resolution_and_regulator_cut.md)
proves transversality of the marked geometric branch to the resolved
complete cut curve, retaining both peripheral normal scales.
