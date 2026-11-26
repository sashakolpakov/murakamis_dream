# Rational boundary transport for the adjacent Fourier kernel

Research deduction, 7 November 2026. The completed adjacent-pair
asymptotic determines an explicit rational relation between boundary
coordinates and derivatives of its action. This note derives that
relation and its composition rule. It also proves that the current
local Fourier neighborhood cannot be reused unchanged when two
copies of the kernel are joined.

This is a statement about the specified finite source and its
critical action. It neither identifies a knot's peripheral
A-polynomial nor proves a new knot volume limit. No numerical
evaluation is used.

## 1. Coordinates and the selected action

Use the [joint kernel theorem](research_mixed_two_adjacent_joint_outer_packet.md):
\[
 V_N(x,y)=h(x)^T A_2^2h(y)
 =N^{-1/2}\mathcal C(x,y)e^{N\mathcal S(x,y)}
                                      (1+O(N^{-1})).
 \tag{1}
\]
Both boundary variables lie in a fixed neighborhood of
\((x_0,x_0)\), and \(\mathcal C\) is nonzero there. Its action is
\[
\begin{split}
 \mathcal S(x,y)&=F(a_\#,s_\#;x,y)+\pi i(x+y),\\
 F(a,s;x,y)&=g(a+s)+g(a+x)+g(s+y)
       -2g(a)-2g(s)-g(x)-g(y)+2\pi ias .
\end{split}
 \tag{2}
\]
The selected point satisfies \(F_a=F_s=0\), with the logarithms
fixed by the original contour proof. Define
\[
 X=e^{-2\pi ix},\quad W=e^{-2\pi iy},\quad
 U=e^{-2\pi ia_\#},\quad V=e^{-2\pi is_\#},\qquad
 p=e^{\mathcal S_x},\quad q=e^{\mathcal S_y}.
 \tag{3}
\]
The symbol \(q\) in this note is a boundary derivative, not the
root of unity at level \(N\).

Since \(e^{g'(z)}=1-e^{-2\pi iz}\), the critical equations give
\[
 (1-UV)(1-XU)=V(1-U)^2,\qquad
 (1-UV)(1-WV)=U(1-V)^2.
 \tag{4}
\]
Differentiating the critical value in (2) gives
\[
 p=-\frac{1-XU}{1-X},\qquad
 q=-\frac{1-WV}{1-W}.
 \tag{5}
\]
The minus signs retain the outside factor \(\pi i(x+y)\).

All rational statements below are on the regular open set where
the displayed denominators and
\(X,W,U,V,p,q,1-U,1-V,1-UV,1-X,1-W\)
are nonzero. This set contains the selected reference point.

## 2. The rational relation and its inverse

**Proposition 1.** On this regular set,
\[
 p=UV\frac{1-U}{1-V},\qquad
 q=UV\frac{1-V}{1-U},\qquad pq=(UV)^2.
 \tag{6}
\]
In particular the second boundary pair is a rational function of
the first. Put
\[
 U=\frac{1+p(1-X)}{X},\qquad D=p+U(1-U).
\]
Then
\[
 V=\frac pD,\qquad q=\frac{U^2p}{D^2},\qquad
 W=\frac{1+q}{q+V}.
 \tag{7}
\]
Restrict further to \(D(q+V)\ne0\). These formulas define a
birational map
\[
                  \mathcal R:(X,p)\longmapsto(W,q)
 \tag{8}
\]
whose inverse is the same formula with the two boundaries
exchanged. Thus \(\mathcal R^2\) is the identity wherever
both compositions are defined.

*Proof.* The first equation in (4) implies
\[
 1-X=-\frac{(1-U)(1-V)}{U(1-UV)}.
\]
Substitution in (5) proves the first equation in (6); the
other follows by exchanging the two boundaries. Their product
gives the last equation.

The first equation in (5) recovers \(U\) as in (7).
Next \(p(1-V)=UV(1-U)\), so \(V=p/D\).
The product relation yields \(q=U^2p/D^2\), and the second
equation in (5) gives \(W=(1+q)/(q+V)\).

Conversely, these formulas imply (5) and (6); substituting
them gives (4). Exchanging the boundaries recovers \(V\),
then \(U\), and then \(X,p\). This proves the inverse
assertion on the stated regular open set. \(\square\)

The algebraic equations do not fix logarithmic lifts.
For the selected analytic branch, the original equations
\(F_a=F_s=0\) still have to hold, not merely their
exponentials (4).

## 3. The differential form and orientation

Give the boundary torus coordinates the two-form
\[
                         \omega=d\log p\wedge d\log X.
\]
The correspondence satisfies
\[
       d\log p\wedge d\log X+
                      d\log q\wedge d\log W=0.
 \tag{9}
\]
Thus boundary exchange (8) reverses this form. The directed
transport uses the reciprocal incoming derivative:
\[
 (X,P)\longmapsto(W,Q)=\mathcal R(X,P^{-1}),\qquad Q=q.
 \tag{10}
\]
It preserves the form:
\[
                     d\log Q\wedge d\log W
                              =d\log P\wedge d\log X.
 \tag{11}
\]

Here is a derivation that also checks that the relation has
the expected local dimension. On the selected branch,
\(d\mathcal S=\log p\,dx+\log q\,dy\), so its exterior
derivative is zero. Since \(d\log X=-2\pi i\,dx\) and
\(d\log W=-2\pi i\,dy\), this is (9).

Moreover, if \(H=F''\) denotes the Hessian in \(a,s\), then
\[
 \mathcal S_{xy}
 =\frac{g''(a_\#+x)\,g''(s_\#+y)
                 \{g''(a_\#+s_\#)+2\pi i\}}{\det H}
 \ne0.
 \tag{12}
\]
Indeed \(g''(z)=2\pi i Z/(1-Z)\), with
\(Z=e^{-2\pi iz}\), and
\(g''(a_\#+s_\#)+2\pi i=2\pi i/(1-UV)\).
Every numerator factor is nonzero on the regular set,
and \(\det H\ne0\) by the joint kernel theorem.
Consequently \((x,y)\mapsto(X,p)\) is locally invertible.
Equation (9) therefore holds on an open set in the
rational coordinates of (8), and hence as a rational
differential identity. Inverting \(p\) proves (11).

The involution in (8) exchanges boundaries. It does not
make the directed map (10) an involution or prove that
its iterates eventually simplify. Such a conclusion
would require a separate argument.

## 4. The matching condition for an actual composition

The original Fourier vectors have the exact bilinear identity
\[
                 N\int_\Gamma h(z)h(z)^T\,dz=I_N
 \tag{13}
\]
on any full horizontal period, at both level parities.
Therefore
\[
 h(x)^TA_2^4h(y)
       =N\int_\Gamma V_N(x,z)V_N(z,y)\,dz.
 \tag{14}
\]
No complex conjugation occurs in this formula.

Where both selected local phases apply, stationarity of
the joined phase requires
\[
 \mathcal S_y(x,z)+\mathcal S_x(z,y)=0.
 \tag{15}
\]
In the rational coordinates this implies
\[
                         q_{\rm left}p_{\rm right}=1.
 \tag{16}
\]
The reciprocal incoming derivative in (10) is precisely
the orientation required by this equation. Equation (16)
alone only fixes (15) modulo \(2\pi i\).

At the reference point \(x=y=x_0\), symmetry gives \(U=V\),
and (6) gives \(p=q=U^2\). Write
\(a_*=\alpha+ih_*\). The
[critical-point bounds](research_mixed_two_adjacent_critical_corridor.md)
give \(h_*>1/20\). Hence
\[
 \Re\mathcal S_x(x_0,x_0)
  =\Re\mathcal S_y(x_0,x_0)=4\pi h_*>\frac{\pi}{5}.
 \tag{17}
\]
For the composition (14), at \(x=z=y=x_0\),
\[
 \Re\{\mathcal S_y(x,z)+\mathcal S_x(z,y)\}
                    =8\pi h_*>\frac{2\pi}{5}.
 \tag{18}
\]
Continuity gives a neighborhood of this triple on which
the real part remains positive. Thus there is no joined
critical point in that neighborhood.

This does not exclude a critical point elsewhere, another
representation, or cancellation among the complementary
parts of (14). The ordinary same-sign chain is already
covered by the
[internal-chain theorem](research_internal_two_crossing_chain.md).
What (18) excludes is the shortcut of reusing the present
local Fourier neighborhood as though it were preserved
under joining. A useful general transport theorem must
locate the new matched branch and control its complete
integration cycle.

