# Eigenline transport through an ordered half twist

1 November 2026. A local calculation for the marked geometric construction.

The pure two-octahedron calculation gives the correct local peripheral
matrices. To join these calculations, one must also keep track of the
eigenlines selected by the oriented main strands. A half twist exchanges
the strands. If the two displayed puncture flags select opposite
eigenvalues, it exchanges the two eigenline choices as well. The formulas
below record that exchange instead of replacing it by a scalar.

Everything here is an identity of two-dimensional linear maps. The final
section states the further topological information needed to apply it to
the original knot. In particular this note does not prove a global
longitude formula.

## 1. Reversing a path and changing the eigenline

Let \(g\in\mathrm{SL}_2(\mathbb C)\) transport a puncture matrix
\(A_p\) to \(A_q\), so that \(gA_pg^{-1}=A_q\). Suppose their
eigenvalues are \(\lambda,\lambda^{-1}\), with
\(\lambda^2\ne1\). Choose eigenvectors at each end with
\[
 \det(v_p^+,v_p^-)=\det(v_q^+,v_q^-)=1.
 \tag{1}
\]
If \(gv_p^+=c v_q^+\), preservation of the determinant forces
\(gv_p^-=c^{-1}v_q^-\). Consequently
\[
                     g^{-1}v_q^-=c v_p^- .
 \tag{2}
\]
Thus reversing the path and exchanging its eigenline preserves its
transport coefficient in these determinant-normalized frames. The
exchange is essential: reversing the path on the same eigenline gives
\(c^{-1}\).

The frames in (1) can become singular when the two eigenlines coalesce.
This does not justify evaluating their separate coefficients at a
parabolic point. A closed product which is a holomorphic matrix
eigenvalue can instead be continued to that point after the frame
factors have cancelled.

There is also a useful two-point form of the same cancellation. For
independent flags represented by \(a,b\), every invertible matrix
\(T\) satisfies
\[
             (Ta)\wedge(Tb)=\det(T)(a\wedge b).
 \tag{3}
\]
In affine coordinates, when the displayed denominators are nonzero,
this says
\[
 T'(z_1)T'(z_2)
       =\left(\frac{T(z_1)-T(z_2)}{z_1-z_2}\right)^2.
 \tag{4}
\]
Equation (3) is valid in every projective coordinate chart. It is the
appropriate form for cancelling a common seam frame at its two main
punctures. It does not decide which two flags the original paths use.

## 2. The ordered collar map

Take \(A,B\in\mathrm{SL}_2(\mathbb C)\) with equal trace, and put
\[
       P=BA,\qquad K=P^{-1}-I,\qquad
       \delta=\det K=2-\operatorname{tr}P.
 \tag{5}
\]
Assume \(\delta\ne0\). This holds near the actual complete disk
longitude, where \(\operatorname{tr}P=-2\) and \(\delta=4\).
The equal-trace Cayley--Hamilton identities give
\[
 KB=AK,\qquad KP=PK,\qquad
 KAK^{-1}=A^{-1}BA,
 \qquad K^2=-\delta P^{-1}.
 \tag{6}
\]
For example, \(P^{-1}B=A^{-1}\) and
\(A P^{-1}=B^{-1}\), so
\(KB=A^{-1}-B=A-B^{-1}=AK\), using
\(A+A^{-1}=B+B^{-1}\). Since \(K\) commutes with \(BA\),
the remaining conjugation follows. The last identity is
Cayley--Hamilton for \(P^{-1}\).

The ordered positive collar convention is therefore
\[
                    (A,B)\longmapsto(A^{-1}BA,A).
 \tag{7}
\]
This convention preserves \(BA\). Its inverse is the negative
half twist. It must not be confused with the convention preserving
\(AB\), whose regular conjugator is \(AB-I\).

If \(Aa=\lambda a\) and \(Bb=\lambda b\), with independent
\(a,b\), one obtains the exact tensor identity
\[
 \frac{(Ka)\otimes(Kb)}{\delta}
              =-\lambda^{-1}(A^{-1}b)\otimes a.
 \tag{8}
\]
To check it, use \(a,b\) as a basis. The two matrices then have
the form
\[
 A=\begin{pmatrix}\lambda&\alpha\\0&\lambda^{-1}\end{pmatrix},
 \qquad
 B=\begin{pmatrix}\lambda^{-1}&0\\\beta&\lambda\end{pmatrix}.
 \tag{9}
\]
Here \(K=\left(\begin{smallmatrix}\alpha\beta&-\alpha/\lambda\\
 -\beta\lambda&0\end{smallmatrix}\right)\),
\(\delta=-\alpha\beta\),
\(Ka=-\beta A^{-1}b\), and
\(Kb=-\alpha\lambda^{-1}a\). These are precisely (8).

The two eigenvalues in the hypothesis of (8) must be the same. In the
native geometric chart the two ideal flags on a disk side can select
opposite eigenvalues. In that case (8) is not a formula for their
transport.

## 3. A transport operator which retains both choices

The two actual strand paths in (7) carry \(b\) to \(A^{-1}b\)
and \(a\) to \(a\). These are paths on different strands; they
are not the simultaneous conjugation by \(K\). The latter identifies
the outgoing puncture representation with the incoming one. Keeping
both operations gives the linear map
\[
 \mathscr B
   =\delta\,(K^{-1}A^{-1}\otimes K^{-1})\,\mathsf s,
 \qquad \mathsf s(a\otimes b)=b\otimes a.
 \tag{10}
\]
The order of the two factors records the two ordered outgoing
punctures. Formula (10) is unchanged if \(K\) is multiplied by a
nonzero scalar. It is holomorphic wherever \(\delta\ne0\),
including the noncentral parabolic point. No square root of a
determinant or diagonalization is required to define it.

It has the exact full-twist identity
\[
                         \mathscr B^2=A\otimes B.
 \tag{11}
\]
Indeed \(K^{-1}A^{-1}=B^{-1}K^{-1}\) by (6), and
\(K^{-2}=-P/\delta\). Squaring (10) therefore gives
\[
 \begin{aligned}
 \mathscr B^2
 &=\delta^2
  (K^{-1}A^{-1}K^{-1})\otimes(K^{-2}A^{-1})\\
 &=\delta^2(-A/\delta)\otimes(-B/\delta)
  =A\otimes B.
 \end{aligned}
 \tag{12}
\]
This holds for arbitrary equal-trace \(A,B\) satisfying (5), not
only for a selected eigenline. It also gives all integer powers:
\[
 \mathscr B^{2j}=(A\otimes B)^j,\qquad
 \mathscr B^{2j+1}=\mathscr B(A\otimes B)^j,
 \qquad j\in\mathbb Z.
 \tag{13}
\]

For a more explicit description, use (9), put
\(h=\lambda-\lambda^{-1}\), and choose
\[
 a_+=\binom10,\quad a_-=\binom{-\alpha}{h},\qquad
 b_+=\binom01,\quad b_-=\binom h{-\beta}.
 \tag{14}
\]
The subscripts denote eigenvalues \(\lambda^{\pm1}\) of the
corresponding puncture. When \(h\ne0\), these give bases. Direct
substitution in (10) yields
\[
 \begin{aligned}
 \mathscr B(a_+\otimes b_+)&=-\lambda\,a_+\otimes b_+,\\
 \mathscr B(a_-\otimes b_-)&=-\lambda^{-1}a_-\otimes b_-,\\
 \mathscr B(a_+\otimes b_-)&=
       -\frac{\lambda\beta}{\alpha}\,a_-\otimes b_+,\\
 \mathscr B(a_-\otimes b_+)&=
       -\frac{\alpha}{\lambda\beta}\,a_+\otimes b_-.
 \end{aligned}
 \tag{15}
\]
The two mixed coefficients are reciprocal. A full twist is the identity
on these two mixed states, while on the equal-eigenvalue states it
acts by \(\lambda^2\) or \(\lambda^{-2}\). A half twist
exchanges the mixed states. Replacing it by either of its equal-state
scalars would erase this exchange and generally give a wrong gluing.

Rescaling the four eigenvectors changes the two mixed coefficients
reciprocally. For instance, replacing \(a_-\) by
\((-\lambda\beta/\alpha)a_-\) makes both mixed coefficients
one. This is a change of local frames, not a proof that their factors
cancel in a closed knot. The original seam identifications must use
the same frames for such a cancellation to be valid.

## 4. What a global application still requires

Equations (2)--(4) justify cancellation of seam frames once the actual
oriented paths and their eigenlines have been specified. Equations
(10)--(15) give an explicit way to keep a half twist when those lines
are exchanged. They supply the missing local algebra needed for that
bookkeeping; they do not choose the bookkeeping for the knot.

For the original ordered tree one must still show that its successive
page attachments use these exact path identifications, and that the
chosen main eigenlines close after following the oriented knot. Only
then may one multiply the local longitude factors, remove internal
frame changes, and apply the preferred-framing correction. The
canonical pure block and its corrected nonparabolic source coordinate
have been checked separately. The mixed-state exchange above explains
why their global odd extension needs an explicit argument.
