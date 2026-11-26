# Modulus constraints at a selected boundary maximizer

Research deduction, 6 November 2026. This note retains the stationary
equations of the original first-four/next-three phase when estimating
its optimizing height curvature. It proves a necessary scalar
inequality at every factorial maximizer, including its possible
boundary faces, and gives compact cotangent forms of the equations.
It does not prove the remaining curvature determinant or a finite
selected-source estimate.

## 1. The original phase and its one-sided derivatives

Use \(\mathcal F(e,s,z,b)\), the fixed actual heights, and the
original outgoing affine subtraction from
[the height-envelope proof](research_mixed_selected_boundary_height_envelope.md).
The first vertex is type four, the next vertex is ordinary type three,
and the word has length at least three. The changing height is
\(k=\Im z\); the factorial correction \(-2\pi k\) is constant
during horizontal maximization. The real affine subtraction depends
only on \(\Re b\).

The proved whole-path restrictions, including
[the summed-coordinate bound](research_mixed_factorial_next_three_sum_bound.md),
give, at every factorial maximizing point,
\[
 .3<\Re e<.4,\qquad .2<\Re s\le.5,\qquad
 .22\le\Re z<3/8,\qquad .22\le\Re b\le.45.
\tag{1}
\]
The original maximizing box has \(e\)-interval \([.27,.49]\),
\(s\)-interval \([.15,.5]\), and \(z\)-interval \([.22,.45]\).
Consequently, writing \(D_j=\Re\mathcal F_j\), its necessary
first-order conditions include
\[
                       D_e=0,\qquad D_s\ge0,\qquad D_z\le0.
\tag{2}
\]
Indeed \(e\) is strictly interior. A small decrease of \(s\)
is allowed, so its derivative cannot be negative; a small increase
of \(z\) is allowed, so its derivative cannot be positive.
When \(s\) or \(z\) is interior its corresponding inequality
is equality. No stationarity in a constrained coordinate has been
silently imposed.

## 2. A necessary norm inequality, including active faces

Put
\[
 E=e^{-2\pi i e},\quad S=e^{-2\pi i s},\quad
 Z=e^{-2\pi i z},\quad B=e^{-2\pi i b},
 \qquad r_s=|S|,\quad r_z=|Z|,\quad r_b=|B|,
\tag{3}
\]
and define \(N_V=|1-V|^2\) and \(N_{VW}=|1-VW|^2\).
Let \(u=u_c(e)\) be the original canonical endpoint root,
\(W=e^{-2\pi iu}\), and let
\(R_e=\sqrt{E(2-E)}\) denote the canonical square root specified
in [the cap-curvature proof](research_mixed_private_cap_curvature_bound.md).
Set
\[
                     C_e=|1-R_e|^4>0.
\tag{4}
\]
This is a value on the original branch, not a choice of a new root.
The exact private identity
\((1-E)(W-E)=-(1-R_e)^2\), together with the original chirp,
gives
\[
 \begin{split}
 e^{2D_e}&=\frac{N_{EZ}}{C_e},\\
 e^{2D_z}&=\frac{N_{EZ}N_{SZ}}{r_s^2N_Z^3},\\
 e^{2D_s}&=\frac{N_{SZ}N_{SB}}{r_z^2N_S^2}.
 \end{split}
\tag{5}
\]
These follow by taking absolute values of the literal exponentiated
derivatives. In particular the factors \(r_s^2\) and \(r_z^2\)
are the contributions of the original \(2\pi izs\) term.

**Proposition 1.** Every factorial maximizer in (1) satisfies
\[
 \begin{split}
 N_{EZ}&=C_e,\\
 N_{SZ}&\le\frac{r_s^2N_Z^3}{C_e},\\
 N_{SB}&\ge\frac{r_z^2N_S^2}{N_{SZ}}
       \ge M_0:=\frac{r_z^2N_S^2C_e}{r_s^2N_Z^3}.
 \end{split}
\tag{6}
\]
Thus two further necessary conditions are
\[
 \boxed{\displaystyle M_0\le(1+r_sr_b)^2,\qquad
 \cos(2\pi\Re(s+b))
       \le\frac{1+r_s^2r_b^2-M_0}{2r_sr_b}.}
\tag{7}
\]
If both \(s\) and \(z\) are interior, then
\(N_{SZ}=r_s^2N_Z^3/C_e\) and \(N_{SB}=M_0\).

*Proof.* Apply (2) to (5), in the displayed order. Every denominator
is positive: the original regular strips exclude the zeros in
\(N_S,N_Z,N_{SZ}\), all radii are nonzero, and \(R_e=1\)
would imply \(E=1\), which is excluded. The triangle inequality
gives \(N_{SB}\le(1+r_sr_b)^2\). Finally use the exact identity
\[
 N_{SB}=1+r_s^2r_b^2
                   -2r_sr_b\cos(2\pi\Re(s+b)).
\tag{8}
\]
This proves (7) without selecting either sign of
\(\sin(2\pi\Re(s+b))\). \(\square\)

The cosine assertion is valid even when \(\Re(s+b)\le1/2\).
It should not be replaced by an upper bound for the summed angle
without first restricting to a monotone cosine interval. Similarly,
equalities in (6) are not available merely because the entire
maximizer is unique: a coordinate may still be constrained.

## 3. Cotangent and Möbius forms

For compact algebraic expressions write
\[
 p=\cot\pi e,\qquad q=\cot\pi s,\qquad
 r=\cot\pi z,\qquad v=\cot\pi b,
 \qquad T=\sqrt{(p+i)^2+4}.
\tag{9}
\]
The root \(T=R_e(p+i)\) is the canonical first-quadrant root
from the cap-curvature proof. The cotangent-exponential relation
\(E=(p-i)/(p+i)\), and its counterparts, give exactly
\[
 \begin{split}
 e^{D_s}
   &=\frac{|(q+r)(q+v)|}{|(r-i)(v+i)|},\\
 e^{D_z}
   &=\frac{|(p+r)(q+r)(r+i)|}
                {2|(p+i)(q-i)|},\\
 D_e=0\quad&\Longleftrightarrow\quad
 \frac{|p+r|}{|r+i|}
                =\frac8{|p+i|\,|p+i+T|^2}.
 \end{split}
\tag{10}
\]
For the last formula, use
\(1-R_e=(p+i-T)/(p+i)\) and
\((p+i-T)(p+i+T)=-4\). For the first two, substitute
\(1-SZ=2i(q+r)/[(q+i)(r+i)]\) into (5), before taking
the appropriate square root. These substitutions have no vanishing
denominators on the original strips; in particular
\(p+i+T\ne0\) by its product identity.

Introduce the two Möbius variables
\[
                  U_c=\frac{p+r}{p+i},\qquad
                  U_o=\frac{q+r}{q-i}.
\tag{11}
\]
Equations (2) and (10) imply, at every factorial maximizer,
\[
 \begin{split}
 |U_c|&=\frac{8|r+i|}{|p+i|^2|p+i+T|^2},\\
 |U_cU_o|&\le\frac2{|r+i|},\\
 |U_o|&\le\frac{|p+i|^2|p+i+T|^2}{4|r+i|^2}.
 \end{split}
\tag{12}
\]
Both inequalities become equalities when \(z\) is interior.
Thus the modulus of the chirped-pair variable is constrained by
the canonical cap equation; it is not independent cotangent data.

For clarity, if \(q=a+ib\) and \(r=c+id\), then
\[
 \Im U_o
    =\frac{a(1+d)+c(1-b)}{|q-i|^2}>0.
\tag{13}
\]
Here \(a\ge0,c>0,|b|,|d|<1\) on the already-proved
optimizing box, including the face \(\Re s=1/2\).
The [exact pair metric](research_mixed_pair_curvature_composition.md),
Proposition 1, consequently takes the particularly short form
\[
                  \mathcal K_{-1}(s,z)
                         =\frac{2|U_o-1|^2}{\Im U_o}.
\tag{14}
\]
Indeed \(U_o-1=(r+i)/(q-i)\), so (14) is that
proposition's formula with its positive denominator unchanged.

Equation (14) is the metric of the chirped pair alone. The full
metric still includes the private-cap and outgoing-block stiffness
and the shared-coordinate correction. In particular, a modulus
bound in (12) does not by itself bound (14), since it supplies no
positive lower bound for \(\Im U_o\).

The [active-face response criterion](research_mixed_active_face_curvature_budget.md)
separately uses \(D_s=0\) and the original outgoing marginal to
reconstruct the outgoing coordinate when both are free. That
condition, the actual rational reference curve and its next-external
compatibility remain part of any application. The inequalities here
are necessary conditions for the original optimizing problem, not
conditions sufficient to realize a reference by a word or to prove
the outstanding six-pi bound.
