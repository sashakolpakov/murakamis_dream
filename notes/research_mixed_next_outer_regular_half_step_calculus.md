# Regular half-step calculus on the doubled spectral quotient

Private exact-source deduction, 9 November 2026. The standard symmetric
half-step average and divided difference give explicit polynomial maps
between the two spectral factors of the doubled grid. They retain its
endpoint multiplicities and reconstruct the original second-order
Askey--Wilson operator as an ordered polynomial expression. The literal
oriented half-step is recovered only after adjoining its odd angular
coefficient.

This is an application of the ordinary half-step divided-difference
calculus to the specified finite source. It is not an oriented
factorization, an inverse estimate, or a cancellation theorem. No
mathematical numerical evaluation or frozen-source change is used.

## 1. Polynomial operators, including their coalescing limits

Use the [doubled-grid theorem](research_mixed_next_outer_doubled_grid_half_step.md)
with \(N\ge3\), \(\theta=\pi/N\), \(q=e^{i\theta}\),
\(X=-\zeta-\zeta^{-1}\). Put
\[
 c=\cos\theta,\qquad s=\sin\theta,\qquad
 X_+=X(q\zeta),\quad X_-=X(q^{-1}\zeta).
\tag{1}
\]
The two shifted coordinates satisfy
\[
 X_++X_-=2cX,\qquad
 X_+X_-=X^2-4s^2,\qquad
 \frac{(X_+-X_-)^2}{4}=s^2(4-X^2)=:\chi(X).
\tag{2}
\]
For an ordinary polynomial \(f\), define
\[
 \mathsf A f=\frac{f(X_+)+f(X_-)}2,
 \qquad
 \mathsf D f=\frac{f(X_+)-f(X_-)}{X_+-X_-}.
\tag{3}
\]
The second expression is the ordinary polynomial divided difference,
with value \(f'(X_+)\) when \(X_+=X_-\).

Both expressions are symmetric polynomials in \(X_+,X_-\), hence
ordinary polynomials in \(X\) by (2). In particular
\[
 \deg\mathsf A f\le\deg f,\qquad
 \deg\mathsf D f\le\deg f-1
\tag{4}
\]
for nonconstant \(f\), and \(\mathsf D1=0\). Their leading
terms on monomials are
\[
 \mathsf A(X^k)=\cos(k\theta)X^k+O(X^{k-1}),\qquad
 \mathsf D(X^k)=\frac{\sin(k\theta)}{\sin\theta}
                               X^{k-1}+O(X^{k-2}).
\tag{5}
\]
For the second formula at \(k=0\), use \(\mathsf D1=0\)
instead. Formula (5) follows by letting \(\zeta\to\infty\),
when \(X_\pm\sim q^{\pm1}X\). Vanishing of a leading multiplier
only lowers the degree and introduces no division by that multiplier.

The coalescing spectral endpoints are explicit:
\[
 \mathsf A f(\pm2)=f(\pm2c),\qquad
 \mathsf D f(\pm2)=f'(\pm2c).
\tag{6}
\]
Thus there are no rational-coefficient poles to discard at either
endpoint. The derivative in (6) belongs to the interior double node
of the other grid. The polynomial realization, rather than evaluation
of separated singular terms, fixes all further required normals.

## 2. Exact product rules and exchange of the two full ideals

The two-point identities in (3) give
\[
\begin{split}
 \mathsf A(fg)&=(\mathsf A f)(\mathsf A g)
                       +\chi(\mathsf D f)(\mathsf D g),\\
 \mathsf D(fg)&=(\mathsf A f)(\mathsf D g)
                       +(\mathsf D f)(\mathsf A g).
\end{split}
\tag{7}
\]
They hold as ordinary polynomial identities, including coalescing
limits. For example
\[
 \mathsf A(Xf)=cX\mathsf A f+\chi\mathsf D f,
 \qquad
 \mathsf D(Xf)=\mathsf A f+cX\mathsf D f.
\tag{8}
\]

Let \(P=P_N\) and \(R=P(P-4)\). The exact Chebyshev half-step
identity from the doubled-grid theorem is
\(P(X_+)=P(X_-)=4-P(X)\). Consequently
\[
\begin{gathered}
 \mathsf A P=4-P,\qquad \mathsf D P=0,\\
 \mathsf A(Pf)=(4-P)\mathsf A f,
 \qquad \mathsf D(Pf)=(4-P)\mathsf D f,\\
 \mathsf A((P-4)f)=-P\mathsf A f,
 \qquad \mathsf D((P-4)f)=-P\mathsf D f,\\
 \mathsf A(Rf)=R\mathsf A f,
 \qquad \mathsf D(Rf)=R\mathsf D f.
\end{gathered}
\tag{9}
\]

**Proposition 1.** The operators \(\mathsf A,\mathsf D\) descend
to the doubled spectral quotient
\[
 \mathcal V_N=\mathbb C[X]/(P(P-4))
     \simeq\mathcal A_N\oplus\mathcal A_N^{\rm opp}.
\tag{10}
\]
They exchange its two CRT components. More precisely, for
\(e_{\rm orig}=1-P/4\), \(e_{\rm opp}=P/4\), and either
\(\mathsf H=\mathsf A\) or \(\mathsf D\),
\[
 \mathsf H(e_{\rm orig}f)=e_{\rm opp}\mathsf Hf,
 \qquad
 \mathsf H(e_{\rm opp}f)=e_{\rm orig}\mathsf Hf.
\tag{11}
\]
Equivalently they induce maps \(\mathcal A_N\to\mathcal A_N^{\rm opp}\)
and \(\mathcal A_N^{\rm opp}\to\mathcal A_N\), with the full
values and first normals specified by the two ideals.

*Proof.* The last line of (9) proves descent. The preceding lines
or (7) give (11). They also show directly that changing an input
representative by its full defining ideal changes its opposite-grid
output by the opposite full ideal. These are polynomial ideal
identities, so both the interior first normals and the simple
endpoint values are retained. \(\square\)

Neither operator is asserted invertible. They do not turn the
literal half-step into an endomorphism of the original quotient;
they provide regular maps to the opposite quotient and back.

## 3. Reconstruction of the oriented half-step

In the doubled angular algebra
\(\mathcal B_N=\mathbb C[\zeta^{\pm1}]/((\zeta^{2N}-1)^2)\),
the exact decomposition of the literal translations is
\[
\begin{split}
 \tau f
  &=\mathsf A f-
       \frac{(q-q^{-1})(\zeta-\zeta^{-1})}{2}\mathsf D f,\\
 \tau^{-1}f
  &=\mathsf A f+
       \frac{(q-q^{-1})(\zeta-\zeta^{-1})}{2}\mathsf D f,
 \qquad \tau f(\zeta)=f(q\zeta).
\end{split}
\tag{12}
\]
Here \(f\) denotes the pullback of a spectral polynomial. Formula
(12) follows from (3) and
\(X_+-X_-=-(q-q^{-1})(\zeta-\zeta^{-1})\).
It is an ordinary Laurent identity before reduction, so it includes
all angular first jets.

The factor \(\zeta-\zeta^{-1}\) is odd under reflection. It is
exactly the additional angular datum in an oriented half-step that
is absent from the reflection-invariant spectral quotient. Retaining
only \(\mathsf A f\), or identifying \(\tau f\) with an even
polynomial, would change the source map.

## 4. Reconstruction of the original Askey--Wilson operator

The regular calculus recovers the original operator, with its exact
normalization. Put
\[
 \alpha(X)=(1-cX/2)^2+(1-X^2/4)s^2.
\tag{13}
\]
Then, as an ordered ordinary polynomial identity,
\[
\boxed{\quad
 \mathcal L
    =2cI+16s^2\bigl[(1-cX/2)\mathsf A\mathsf D
                              -\alpha(X)\mathsf D^2\bigr].
\quad}
\tag{14}
\]
In (14), \(\mathsf A\mathsf D\) means first apply \(\mathsf D\),
then \(\mathsf A\), and the displayed spectral factors multiply
after those operators. Since each half-step exchanges the two full
ideals, both compositions in (14) preserve each spectral factor.

*Proof.* Write \(X=-2\cos u\). Away from their removable zero
denominators, (3) becomes
\[
 \mathsf D f(u)=
       \frac{f(u+\theta)-f(u-\theta)}{4s\sin u},
 \qquad
 \mathsf A f(u)=\frac{f(u+\theta)+f(u-\theta)}2.
\tag{15}
\]
For \(f(u+2\theta)\), the coefficient on the right of (14) is
\[
 \frac{-\alpha(X)+2s\sin u(1+c\cos u)}
             {\sin u\sin(u+\theta)}
 =-\frac{(1+\cos(u+\theta))^2}
             {\sin u\sin(u+\theta)}
 =-\frac{4\cos^4((u+\theta)/2)}
             {\sin u\sin(u+\theta)}.
\tag{16}
\]
For \(f(u-2\theta)\), the corresponding numerator has the minus
sign before \(2s\sin u(1+c\cos u)\), giving
\(-4\cos^4((u-\theta)/2)/[\sin u\sin(u-\theta)]\).
These are exactly the two shifted coefficients in
[current-free crossing transport, (3)](research_current_free_aw_crossing_transport.md).
Both sides send the constant one to \(2c\), fixing the remaining
unshifted coefficient. They agree away from the finite exceptional
set and hence as ordinary polynomial operators everywhere.
\(\square\)

Equation (14) is a complete realization of the original unweighted
operator in the regular doubled calculus. It supplies neither a
factorization of the cubic transport \(\mathcal D_{3,N}\) nor a
choice of one oriented factor of its principal symbol. A future such
identity must also transport the original crossing and trace, retain
the explicit opposite-grid forcing from the doubled-grid theorem,
and respect the reflection term in (12). No such identity or estimate
is inferred here.
