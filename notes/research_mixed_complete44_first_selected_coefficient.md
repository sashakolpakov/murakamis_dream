# A complete first Fourier coefficient with the second variable selected

Private written deduction, 11 November 2026. The estimates on the
connected first contour now bound an exact coefficient of the original
finite Laurent polynomial. The first variable is integrated over its
entire period. The second variable stays on its selected interval, and
the third stays on its original interval.

This conclusion concerns one of the two first Fourier terms. Their
sum is the complete physical first summation. The complementary term
still requires its negative-height left connection.

## 1. The finite coefficient and its normalization

Fix an actual positive three/four word of length \(m\ge4\), beginning
with \(443\) or \(444\). Write its first three flags as
\((1,1,\beta)\), where \(\beta=0,1\). Retain its original coupled
geometric reference \(r_j\), private critical indices, logarithmic
lifts, and ordinary incoming color \(w\). Set
\[
 P=[11/50,9/20],\qquad H=1/100,\qquad
 y=b+iH,\quad z=v+i\Im r_3,\qquad b,v\in P.
 \tag{1}
\]
The second and third private conditional indices are ordinary also
when \(m=4\). At that length the third outgoing boundary meets the
original terminal transform.

For every integer \(N\ge2\), define
\[
 q_N=e^{-2\pi i/N},\qquad P_j=(q_N;q_N)_j,\qquad
 p_j(X)=(q_NX;q_N)_j .
\]
Here \((a;q)_j=\prod_{k=0}^{j-1}(1-aq^k)\), with empty product one.
All \(P_j\), \(0\le j<N\), are nonzero. Let \(d_N\) be the original
polynomial of degree less than \(N\) satisfying
\(d_N(q_N^j)=P_j^{-1}\). Keep the original complete endpoint
coefficient \(H_N\), and put
\[
\begin{split}
 U_{1,N}(w,X)&=\sum_{i=0}^{N-1}
                  H_N(w,q_N^{-i})\,\frac{p_i(X)}{P_i^2},\\
 C_{\epsilon,N}(X,Y)&=\sum_{j=0}^{N-1}
                  \frac{X^{-j}p_j(X)p_j(Y)}{P_j^{2+\epsilon}},
                       \qquad \epsilon=0,1,\\
 L_N(w;X,Y)&=U_{1,N}(w,X)d_N(X)C_{1,N}(X,Y).
\end{split}
 \tag{2}
\]
These are the exact functions of the
[pointwise prefix theorem](research_mixed_four_four_pointwise_prefix_replacement.md),
with its unchanged endpoint normalization.

For a finite Laurent polynomial, \([X^k]\) denotes its coefficient
of \(X^k\), and \(\operatorname{CT}_X=[X^0]\). Define two polynomials
in \(w,Y\) by
\[
 f^{(0)}_{44,N}(w,Y)=N[X^0]L_N(w;X,Y),\qquad
 f^{(1)}_{44,N}(w,Y)=N[X^N]L_N(w;X,Y).
 \tag{3}
\]
Each has degree at most \(N-1\) in either variable.
The \(X\)-exponents of \(L_N\) lie in \([-N+1,2N-2]\):
the cap and \(d_N\) each have degrees between zero and \(N-1\),
and each row of \(C_{1,N}\) has exponents between \(-j\) and zero.
Thus zero and \(N\) are its only possible multiples of \(N\).
The root-of-unity filter gives exactly
\[
\begin{split}
 f_{44,N}(w,Y)
 &=f^{(0)}_{44,N}(w,Y)+f^{(1)}_{44,N}(w,Y)\\
 &=\sum_{j=0}^{N-1}
       \frac{U_{1,N}(w,q_N^j)}{P_j}C_{1,N}(q_N^j,Y).
\end{split}
 \tag{4}
\]
In particular the selected coefficient \(f^{(1)}_{44,N}\) is not
one half of this physical sum.

For \(X(a)=e^{-2\pi ia}\), ordinary Fourier integration gives
\[
 f^{(1)}_{44,N}(w,Y)
  =N\int_0^1
        U_{1,N}(w,X(a))d_N(X(a))X(a)^{-N}
                          C_{1,N}(X(a),Y)\,da .
 \tag{5}
\]
This identity holds for every \(w,Y\). It is a finite coefficient
identity, so it involves no limiting interchange.

## 2. The original action used for comparison

Let \(J(0)=0\), \(J'(t)=\operatorname{Log}(2\sin\pi t)\), with the
original continuation from \(0<t<1\), and
\(g(t)=J(t)+\pi i(t-t^2)/2\). With the original endpoint action
\(S(e)\), define
\[
\begin{split}
 \Psi(e,z_1)&=S(e)+g(e+z_1)-g(z_1)-g(e)
                                      -\frac{\pi i}{2}(e-e^2),\\
 Q_\epsilon(s;a,b)&=g(s+a)+g(s+b)-(2+\epsilon)g(s)
                                      -g(a)-g(b)+2\pi ias,\\
 F_{123}(e,s_2,s_3;z_1,z_2,z_3)
 &=\Psi(e,z_1)+Q_1(s_2;z_1,z_2)+Q_\beta(s_3;z_2,z_3)\\
 &\hspace{1em}-g(z_1)-g(z_2)-\frac{\beta}{2}g(z_3).
\end{split}
 \tag{6}
\]
The star in \(F_{123,*}\) means evaluation at the unchanged
critical reference of the fixed word. Write
\[
 p_R=g'(s_3^*+r_3)-(1+\beta/2)g'(r_3),\qquad
 \Lambda_{123}(z)=\Re F_{123,*}+\Re\{p_R(z-r_3)\}.
 \tag{7}
\]
All four contour estimates below use this same action, its additive
constant, and its outgoing derivative.

The modulus allocation at the third coordinate is
\[
 D_{\beta,N}(Z)=
 \begin{cases}1,&\beta=0,\\ |d_N(Z)|^{1/2},&\beta=1.\end{cases}
 \qquad Z=e^{-2\pi iz}.
 \tag{8}
\]
It is carried as a nonnegative multiplier. It is not a chosen
holomorphic square root.

## 3. The complete coefficient estimate

**Theorem.** Put \(\delta=1/12800\). For every \(\tau>0\), there
are constants \(C_\tau,A_\tau\), depending on the fixed word but
independent of \(N,b,v,w\), such that
\[
\begin{split}
 &\left|f^{(1)}_{44,N}(w,Y)\,
       d_N(Y)Y^{-N}C_{\beta,N}(Y,Z)\right|D_{\beta,N}(Z)\\
 &\hspace{12mm}\le
 C_\tau N^{A_\tau}
       \exp\{N(\Lambda_{123}(z)-\delta+\tau)\},
 \qquad Y=e^{-2\pi iy}.
\end{split}
 \tag{9}
\]
The bound holds throughout (1), for both level parities and all
real ordinary colors \(w\in[-2,2]\). On a sufficiently small fixed
complex neighborhood of \(-2\), it has the same form. Each fixed
ordinary-color derivative obeys this bound on a smaller
neighborhood, with its own polynomial factor.

*Proof.* The integrand in (5) is a finite Laurent polynomial in
\(X(a)\), so it is entire in the additive variable \(a\).
In particular, negative powers of \(X\) introduce no finite
singularity in \(a\). Cauchy's theorem therefore replaces the
real interval in (5) by the following oriented polygonal path:
\[
\begin{split}
 \mathcal H_+:\quad
 0&\longrightarrow1/10
   \longrightarrow1/10+iH
   \longrightarrow9/20+iH\\
  &\longrightarrow1/2+iH
   \longrightarrow1/2
   \longrightarrow7/8
   \longrightarrow1 .
\end{split}
 \tag{10}
\]
The equality is exact for each finite \(N,w,Y\).

The adjoining factor
\(d_N(Y)Y^{-N}C_{\beta,N}(Y,Z)\) is independent of \(a\).
Multiplying (5) by it, and only then using the triangle inequality
on the deformed path, bounds the left side of (9) by
\[
 N\int_{\mathcal H_+}
 \left|U_{1,N}(w,X)C_{1,N}(X,Y)C_{\beta,N}(Y,Z)
             d_N(X)X^{-N}d_N(Y)Y^{-N}\right|
                    D_{\beta,N}(Z)\,|da|.
 \tag{11}
\]
This passage divides no source value or weight, and remains valid
when any of them vanishes.

The complete product in (11) has the following proved bounds:

| Portion of \(\mathcal H_+\) | Gap below \(\Lambda_{123}\) | Source |
|---|---:|---|
| \(0\to1/10\to1/10+iH\to9/20+iH\) | \(1/400\) | [Left connection](research_mixed_complete44_second_selected_first_left_connection.md), Theorem (39) |
| \(9/20+iH\to1/2+iH\to1/2\) | \(1/12800\) | [Right connections](research_mixed_complete44_second_selected_right_half_connections.md), Theorem 1 |
| \([1/2,7/8]\) | \(1/12800\) | [Real first arc](research_mixed_complete44_second_selected_real_first_arc.md), Theorem (34) |
| \([7/8,1]\) | \(1/200\) | [Near-one first arc](research_mixed_complete44_second_selected_far_first_arc.md), Theorem (31) |

Every entry retains both complete diagonal polynomials, the third
factor, and (8). Their proofs cover all finite rows and contour
corrections before estimating the displayed product. The first
Fourier term is selected throughout (10), as required by (5);
the two real-arc theorems include this choice.

Apply each entry with a prescribed allowance smaller than \(\tau\).
The path has fixed finite length, its four portions are independent
of \(N\), and the additional density in (11) is precisely \(N\).
The maximum of the finitely many polynomial factors absorbs this
density and the path lengths. Their smallest gap is \(\delta\).
This proves (9) for all real \(w\).

For complex colors one may take a common smaller neighborhood from
the four source theorems. Equivalently, the whole expression inside
the modulus in (9) has degree at most \(N-1\) in \(w\); applying
their interval polynomial continuation to the all-real estimate
costs any separately prescribed portion of \(\tau\).
The color-independent multiplier (8) is retained without division.
Cauchy's formula on a smaller neighborhood gives each fixed
derivative. This proves the theorem. \(\square\)

## 4. A subsequent selected second-interval integral

For the same outgoing \(z\), define the exact polynomial
\[
 \mathcal E_{11,\beta,N}(w,Z)
  =N\int_{P+iH} f^{(1)}_{44,N}(w,e^{-2\pi iy})\,
       d_N(e^{-2\pi iy})e^{2\pi iNy}
                       C_{\beta,N}(e^{-2\pi iy},Z)\,dy .
 \tag{12}
\]
Its interval is oriented by increasing real part. This integral
has the original density \(N\,dy\). Combining it with (5) gives
the original two densities \(N^2\,da\,dy\), with no extra scalar.
The estimate (9) is uniform in \(y\) on this interval. Hence
\[
 |\mathcal E_{11,\beta,N}(w,Z)|D_{\beta,N}(Z)
 \le C_\tau N^{A_\tau}
             e^{N(\Lambda_{123}(z)-\delta+\tau)} .
 \tag{13}
\]
The color and parity assertions persist.

The first integration in (12) is complete in the precise sense
of (5): it extracts the full coefficient \([X^N]\) of the
original Laurent polynomial. The second integration still uses
only \(P+iH\). Equation (13) neither adds the complementary
first coefficient \(f^{(0)}_{44,N}\) nor completes the other
second-coordinate contours. Those steps are necessary before
asserting a complete second-period asymptotic or iterating this
estimate through arbitrary short attachments.

## Direct source versions

| Source | SHA-256 |
|---|---|
| research_mixed_four_four_pointwise_prefix_replacement.md | 2a4a86ced4bb326baa2ca24bfd6f9c6846103070f4a0731f663ef6d2303a89b7 |
| research_mixed_complete44_second_selected_first_left_connection.md | f91bbac2d0843fec8fd5e9ddc29b4d35efbbdf708f2e5bd8d4db6c686b58c702 |
| research_mixed_complete44_second_selected_right_half_connections.md | 49358cc1d991a59a8fbf38c64306e9d88e64b127e2e8a5229d741972036d00d5 |
| research_mixed_complete44_second_selected_real_first_arc.md | f9a9a53a68faf11293f8463e713afdb951ffd5cddcf18e8f1dee4d09ff5fb37c |
| research_mixed_complete44_second_selected_far_first_arc.md | f163f164be985de37d8d10485ec0790fe5057496d94030afdf5c7b48658cc8be |

This is a written coefficient identity and contour estimate. No
mathematical numerical evaluation, saved-value arithmetic, test,
import, compilation, or frozen-source change is used.
