# Height transport for either terminal transform

Research deduction, 5 November 2026. The two terminal polynomials have
different internal sums, but the same dependence on their incoming
variable. This gives a common height-transport argument. Its type-three
application is unconditional by the completed terminal theorem. Its
type-four application remains conditional on the twenty-one source
comparisons; no incomplete certificate is used as a bound.

## 1. The common incoming factor

Put
\[
 r=e^{-2\pi i/N},\qquad P_i=(r;r)_i,\qquad
 p_i(X)=(rX;r)_i,\qquad X=e^{-2\pi ia}.
\]
The two exact terminal transforms are
\[
 V_{\epsilon,N}(w,X)=\sum_{i=0}^{N-1}
       \frac{X^{-i}p_i(X)}{P_i^{1+\epsilon}}
                         U_{\epsilon,N}(w,r^i),
                 \qquad \epsilon=0,1.
 \tag{1}
\]
Here \(\epsilon=0\) denotes terminal type three and
\(\epsilon=1\) denotes terminal type four. The ordinary color is
\(w\); the complete color is \(w=-2\). The polynomials
\(U_{\epsilon,N}\) are the complete first-cap polynomials, with
their original rows retained. Formula (1) is the
[exact terminal contraction](research_mixed_reversed_cap_assembly.md).

Fix an actual incoming leg of type three, belonging to an open word
of length at least two. Write its original critical value as
\(a_*=A+ic\). Both ordinary and attached inputs are included, so
\(-.072<c<.068\). Set
\[
 I_3=[.267,.433],\qquad a_k=y+ik,\quad y\in I_3,
 \quad k\in[\min(c,0),\max(c,0)].
 \tag{2}
\]
Let \(\mathcal P_\epsilon\) be the original terminal critical
action and define
\[
 \begin{split}
 B_\epsilon(a_*;y)&=\Re\mathcal P_\epsilon(a_*)+
       \Re\mathcal P_\epsilon'(a_*)(y-A)
                         -\kappa(y-A)^2,\qquad
                         \kappa=1/2500000,\\
 A_c(k)&=\begin{cases}
 0,&c\le0,\ c\le k\le0,\\
 \pi(c-k),&c\ge0,\ 0\le k\le c.
 \end{cases}
 \end{split}
 \tag{3}
\]
The incoming type is three even when the terminal type is four.
Consequently there is no incoming Fourier halfweight in this result.

## 2. Transport of each term in the contour decomposition

Every phase of a complex transform-index current in either terminal
proof depends on \(a\) through
\[
              g(a+t)-g(a)+2\pi iat,
       \qquad g(z)=J(z)+i\pi z(1-z)/2.
 \tag{4}
\]
Here \(J'(z)=\log(2\sin\pi z)\) on the original regular
sine strip, and \(t\) is the transform index divided by \(N\).
All these complex currents have
\(t\in[.15,.5]+i[-.12,.12]\). Their other indices do not
occur in (4). Differentiation gives the exact identity
\[
 \partial_a(4)=g'(a+t)-g'(a)+2\pi it
    =\log_{\rm R}(C+P)-\log_{\rm R}(C-i),
       \qquad C=\cot\pi t,\quad P=\cot\pi a.
 \tag{5}
\]
The logarithms retain the original lift; the notation
\(\log_{\rm R}\) denotes their continuation in the right
half-plane, with its continuous boundary values where needed.

The scalar bounds in the
[type-three height-transport proof, Section 2](research_mixed_terminal_three_height_transport.md)
apply on exactly (2): writing \(P=p+i\beta\), one has
\(0<p<1\) and \(\beta>-.37\). Write \(C=u+iv\).
For \(\Re t<.5\), \(u>0\), and the imaginary numerator
of \((C+P)/(C-i)\) is
\[
                       u(1+\beta)+p(1-v).
 \tag{6}
\]
It is positive for \(v\le1\). For \(v>1\), the same
cotangent bound gives \((v-1)/u<7/16<.63\), so it remains
positive. At \(\Re t=.5\), \(u=0\) and \(|v|<1\),
which also gives positivity. The logarithmic difference in (5)
therefore has imaginary part strictly between zero and \(\pi\).
Integrating in the direction specified in (2) proves, for every
such current phase \(\Psi\),
\[
 \Re\Psi(a_k;\hbox{internal indices})
 \le \Re\Psi(y+ic;\hbox{the same indices})+A_c(k).
 \tag{7}
\]
Alias penalties depend only on the internal indices and are unchanged.
All factorial arguments remain on the original regular compact sets.

For a physical transform row, its entire incoming dependence is
the literal polynomial factor \(X^{-i}p_i(X)\). Put
\[
 \mathsf P_\rho(x)=
       \frac{1-\rho^2}{1+\rho^2-2\rho\cos(2\pi x)}>0,
                         \qquad 0<\rho<1.
\]
Logarithmic differentiation of the finite product gives
\[
 \partial_k\log|X^{-i}p_i(X)|=
 \begin{cases}
 -\pi i-\pi\displaystyle\sum_{j=1}^i
                  \mathsf P_{e^{2\pi k}}(y+j/N),&k<0,\\
 -\pi i+\pi\displaystyle\sum_{j=1}^i
                  \mathsf P_{e^{-2\pi k}}(y+j/N),&k>0.
 \end{cases}
 \tag{8}
\]
Thus, with \(X_k=e^{-2\pi ia_k}\),
\[
 |X_k^{-i}p_i(X_k)|
       \le e^{NA_c(k)}|X_c^{-i}p_i(X_c)|.
 \tag{9}
\]
The case \(k=0\), including any new zero of the product, follows
by continuity. The case \(i=0\) is immediate. Formula (9) is
unchanged by the denominator \(P_i^{1+\epsilon}\), by a
coherent inner cap, or by a positive majorant of its inner sum.

## 3. The resulting finite-source theorem

**Theorem.** Assume the complete current and physical-sector bounds
in the terminal source proof for type \(3+\epsilon\), at the
original height \(c\). Then, for every \(\tau>0\), there
are a fixed ordinary-color neighborhood and constants such that
\[
 |V_{\epsilon,N}(w,e^{-2\pi ia_k})|
 \le C_\tau N^{d_\tau}
       \exp N\{B_\epsilon(a_*;y)+A_c(k)+\tau\}.
 \tag{10}
\]
The estimate holds at all sufficiently large integer levels of both
parities. Every fixed ordinary-color derivative satisfies the same
rate on a smaller color neighborhood, with a polynomial prefactor.

*Proof.* Keep the original cuts, heights and residue contours. For
each current with complex transform index use (7). For a physical
transform row use (9) before applying its proved row bound or its
positive majorant. In particular an inner cap that was bounded
coherently is kept whole; a bound for it is never applied to a
restricted inner sum.

For type four the disjoint partition is explicit in
[whole-polynomial assembly, Section 2](research_mixed_terminal_four_full_completion.md).
The initial coherent rows, the small transform strip, and the upper
physical triangle use (9). The central double-residue currents and
the transform contours for the private tails use (7). Every part of
that partition is therefore covered. The corresponding type-three
partition is recorded in the preceding height-transport theorem.

The contour symbols have polynomial prefactors uniformly on the
new incoming compact set. Choose their total rate tolerance to be
less than \(\tau\) and sum the finitely many families. Cauchy's
formula on a smaller fixed color disk treats the derivatives. This
proves (10). It does not infer a bound for a changed-height sum from
a bound for that sum at one height alone: the argument transports
each term of its exact decomposition. \(\square\)

For \(\epsilon=0\), the hypotheses are proved by the
[complete type-three terminal theorem](research_mixed_terminal_three_full_completion.md).
For \(\epsilon=1\), they follow from Condition C of the
type-four whole-polynomial assembly and remain conditional until its
complete certificate and saved replay pass.

## 4. A consequence for the first boundary region

Consider a word of length three with types \((3+\alpha,3,4)\),
where \(\alpha=0,1\). In its contracted integrand, the second
coordinate is a type-three incoming leg for \(V_{1,N}\).
The proved first-pair comparison, including the entire first cap,
the first conditional sum and both permitted first selections, has
the bound
\[
 U_{\alpha0}(k)+A_{c_2}(k)
 <M_{12}+p(y_2-a_2)-\delta_{\alpha0},
 \qquad \delta_{00}=3/100,\quad\delta_{10}=3/125.
 \tag{11}
\]
Here \(U_{\alpha0}(k)\) denotes that first-pair upper rate,
not the polynomial in (1); \(M_{12}\) is its original reference
action and \(p\) its real derivative at the outgoing cut. This is
the first-pair statement used in
[the type-three terminal collar proof, Section 5](research_mixed_terminal_three_height_transport.md).
Its hypotheses concern the first two vertex types and the actual
ordinary second leg, which are unchanged here.

Multiplying its finite bound by (10), with \(\epsilon=1\),
cancels the cut derivative by
\(p+\Re\mathcal P_1'(r_2)=0\). The reference actions add
to \(M_{\rm open}\). One total tolerance less than \(1/250\)
leaves loss \(1/50\) for this entire first-boundary sector.
This conclusion is conditional only on the stated complete type-four
terminal comparisons. It includes the terminal polynomial whole;
it does not cover other boundary regions or prove an asymptotic for
the complete open word. No statement for a selected type-four
incoming leg, or for a real incoming coordinate near zero, follows
from (10).
