# A coherent Newton reduction of the terminal type-three polynomial

Research deduction, 5 November 2026. The type-three terminal polynomial
admits an exact reduction which sums its private endpoint index before
any absolute value. The result uses the original type-four conditional
kernel and the unsummed ordinary Newton data. It is a whole-polynomial
identity, including both parities and ordinary derivatives. No global
upper bound or noncancellation theorem for the remaining sum is asserted.

## 1. The exact reduction

Retain the notation of the
[coherently summed terminal boundary](research_mixed_reversed_cap_assembly.md):
\[
\begin{split}
r=e^{-2\pi i/N},\qquad q=e^{\pi i/N},\qquad
P_j=(r;r)_j,\qquad p_j(X)=(rX;r)_j,\\
C_{\epsilon,N}(X,Y)
 =\sum_{i=0}^{N-1}\frac{X^{-i}p_i(X)p_i(Y)}{P_i^{2+\epsilon}},\\
\mathcal V_{\epsilon,N}(w,X)
 =\sum_{i=0}^{N-1}\frac{X^{-i}p_i(X)}{P_i^{1+\epsilon}}
                         \mathcal U_{\epsilon,N}(w,r^i).
\end{split}
\tag{1}
\]
All factorial indices in denominators are less than \(N\).
The Newton polynomials \(e_l(w)\) and the cap \(\mathcal U\)
are the literal original finite sources.

**Theorem 1.** For every level \(N\ge2\), every ordinary color \(w\),
and every nonzero \(X\),
\[
\boxed{\quad
\mathcal V_{0,N}(w,X)
 =N\sum_{l=0}^{N-1}
       \frac{(-q)^{-l}e_l(w)}{P_l}\,C_{1,N}(X,r^l).
\quad}
\tag{2}
\]
Both sides have Laurent band contained in \([-N+1,0]\).
Thus (2) can be substituted into the exact remaining torus integral,
on arbitrary nonzero circle radii, without a new interpolant or a
change in the other Fourier weights.

*Proof.* The
[physical type-three cap reduction](research_mixed_three_first_cap_packet.md#1-exact-reduction-of-the-original-source)
holds for the whole ordinary polynomial:
\[
\mathcal U_{0,N}(w,r^i)
 =\frac{N}{P_i}\sum_{l=0}^{N-1}
             \frac{(-q)^{-l}e_l(w)}{P_l^2}\,p_l(r^i).
\tag{3}
\]
The terms with \(i+l\ge N\) vanish exactly. For every pair
\(0\le i,l<N\),
\[
                    P_i\,p_l(r^i)=P_l\,p_i(r^l).
\tag{4}
\]
Below the support wall both sides equal \(P_{i+l}\);
on or above it both finite products contain \(1-r^N\).
Substitute (3) into (1), interchange the finite sums, and use (4):
\[
\begin{split}
\mathcal V_{0,N}(w,X)
 &=N\sum_l\frac{(-q)^{-l}e_l(w)}{P_l^2}
       \sum_i\frac{X^{-i}p_i(X)p_l(r^i)}{P_i^2}\\
 &=N\sum_l\frac{(-q)^{-l}e_l(w)}{P_l}
       \sum_i\frac{X^{-i}p_i(X)p_i(r^l)}{P_i^3}.
\end{split}
\tag{5}
\]
The inner sum is precisely \(C_{1,N}(X,r^l)\).
This proof does not divide by any Newton value or Pochhammer zero.
Differentiating (2) in \(w\) therefore retains all ordinary jets,
including jets at physical zeros. \(\square\)

This identity is not a replacement of a type-three vertex by an
independent type-four geometric vertex. Its factor \(N\), Newton
coefficient and complete remaining sum are indispensable.
In particular, the right side must not be replaced by a single
type-four packet at an arbitrarily chosen second argument.

## 2. The reduced original phase and its remaining contour problem

At the complete color, on the regular lower Newton-index strip, use
\[
g(z)=J(z)+\frac{i\pi}{2}(z-z^2),\qquad
V_0(u)=-2J(1/2-u)-2J(u).
\tag{6}
\]
With \(X=e^{-2\pi ia}\), write \(t=i/N\) for the conditional
index and \(u=l/N\) for the Newton index in (5).
The original lifted order-\(N\) phase is
\[
\begin{split}
\mathcal T(a;t,u)
={}&V_0(u)+g(t+a)+g(t+u)-3g(t)\\
   &-2g(u)-g(a)+i\pi u+2\pi iat.
\end{split}
\tag{7}
\]
The \(+i\pi u\) is the same lift of the literal
\((-1)^l\) factor as in the physical cap reduction.
The remaining factor \(q^{-l}\) has order-one logarithm.
Formula (7) is asserted only in the original regular factorial and
Newton-index strips; (2) itself is global and retains every other row.

Let \(T(z,u)\) be the calibrated reduced cap phase from that theorem.
Its displayed formula gives the exact identity
\[
\mathcal T(a;t,u)
 =T(t,u)+g(a+t)-g(a)-g(t)+2\pi iat.
\tag{8}
\]
Thus the reduction preserves the shared-boundary chirp and the original
cap action; it does not replace the coherent cap by its private-row
absolute profile. The last three factorial terms in (8), together with
the chirp, are the original Gram-pair action on its regular strip.

The two stationary equations of the reduced phase are explicitly
\[
\begin{split}
0={}&g'(a+t)+g'(u+t)-3g'(t)+2\pi ia,\\
0={}&2\Log(2\cos\pi u)+g'(u+t)
           -4\Log(2\sin\pi u)+2\pi iu .
\end{split}
\tag{9}
\]
The second follows from \(V_0'=2\Log(2\cos\pi u)
-2\Log(2\sin\pi u)\) and
\(g'=\Log(2\sin\pi u)+i\pi(1/2-u)\).
These are original logarithmic equations, rather than an
exponent-only choice of a stationary branch.

For fixed \(l\), the conditional sum in (5) terminates exactly at
\(i=N-1-l\), even when \(X\) is off the physical grid.
The full remaining parameter triangle is therefore
\[
                 i\ge0,\qquad l\ge0,\qquad i+l<N .
\tag{10}
\]
There is no revived conditional row past this particular wall, because
its second argument is the physical value \(r^l\).
The whole Newton sum still includes both halves and every endpoint;
its zeros at odd levels do not justify deleting their ordinary jets.

Equation (2) gives a concrete alternative source for a coherent
terminal estimate: analyze the original two-index sum (5), with phase
(7) where regular, and its full triangular complement (10).
Existing conditional packets control only their admitted parameter
sets. They do not by themselves bound the whole \(l\)-sum or its
deformed contour. The complete kernel, rather than the separate
homogeneous Gram packet, occurs in (2), so no forbidden regular
Gram approximation has been introduced.

The identity is exact progress on the terminal source. A supporting-plane
bound for \(\mathcal V_0\), its nonzero complete contribution, the
type-four analogue, and the global ordinary-closure theorem remain
separate analytic tasks.
