# Exact Fourier contraction for mixed three- and four-crossing tangles

Research proof, 4 November 2026. Frozen manuscripts are unchanged.

The two tangle kernels have a common finite basis in their boundary
variables. Integrating a shared boundary in this basis gives an explicit
matrix, with a triangular support condition. Consequently any finite
word in the two kernels can be contracted exactly before applying an
asymptotic estimate. This keeps the cancellations in a full Fourier
period; it does not replace that period by a neighborhood of a saddle.

## 1. A common boundary basis

Fix an integer level \(N\ge2\), and put
\[
 q=e^{\pi i/N},\quad Q=q^2,\quad r=Q^{-1},\quad D=N-1,
 \qquad P_j=(r;r)_j=\prod_{a=1}^j(1-r^a),\quad P_0=1.
 \tag{1}
\]
Only indices \(0\le j<N\) occur, so these constants are nonzero.
For \(X=e^{2\pi ix}\), define
\[
 c_x=\frac{e^{-\pi iDx}(1-X^N)}N,
 \qquad f_j(x)=\frac{c_xX^j}{(X;r)_{j+1}},
 \qquad f(x)=(f_0(x),\ldots,f_D(x))^T.
 \tag{2}
\]
The apparent poles are removable. Indeed
\[
 f_j(x)=\frac{e^{-\pi iDx}}N F_j(X),\qquad
 F_j(X)=X^j\prod_{a=j+1}^{N-1}(1-Xr^a).
 \tag{3}
\]
Thus each \(f_j\) is an entire finite Fourier function. Its frequencies
belong to \(-D/2+\{0,\ldots,D\}\). At odd levels they are integers;
at even levels they are half-integers. Products of two such functions
are periodic with period one in either case. The different lowest
degrees of the polynomials \(F_j\) also show that they form a basis.

All integrals below are over one horizontal period, with increasing
real coordinate. The chosen height is arbitrary. Define the bilinear
Gram matrix, without complex conjugation, by
\[
                  \Gamma_{jk}=N\int_0^1 f_j(z+ih)f_k(z+ih)\,dz.
 \tag{4}
\]
Periodicity and holomorphy make this independent of \(h\).

## 2. The exact shared-boundary integral

**Theorem 1.** For \(0\le j,k<N\),
\[
 \Gamma_{jk}=
 \begin{cases}
 \displaystyle\frac{Q^{jk}P_{j+k}}{P_j^2P_k^2},&j+k<N,\\[2mm]
 0,&j+k\ge N.
 \end{cases}
 \tag{5}
\]
Equivalently, it is the polynomial Gaussian binomial coefficient
\({j+k\brack j}_Q\), evaluated at the primitive root \(Q\), divided
by \(P_jP_k\). In particular the support cutoff is an exact zero,
not an exponentially small error.

*Proof.* Retain the original Newton crossing matrix \(M\), its scalar
\(\kappa=q^{D^2/2}\), and half-band cardinal vector \(h(x)\).
The [exact crossing calculation](research_three_four_source_interface.md)
gives
\[
 (Mh(x))_j=\kappa(-q)^jP_j f_j(x),\qquad
 M_{j\ell}=\kappa(-1)^j q^{j+\ell^2}{j\brack\ell}_Q
                     \quad(0\le\ell\le j).
 \tag{6}
\]
The cardinal identity is \(N\int h(z)h(z)^Tdz=I_N\). Substituting
(6) in (4) therefore yields
\[
 \Gamma_{jk}=
 \frac1{P_jP_k}\sum_{\ell=0}^{\min(j,k)}
                     Q^{\ell^2}{j\brack\ell}_Q{k\brack\ell}_Q
 =\frac1{P_jP_k}{j+k\brack j}_Q.
 \tag{7}
\]
Here the final identity is the finite q-Vandermonde identity. For an
elementary proof at an indeterminate \(Q\), take the coefficient of
\(z^j\) in
\[
 \prod_{a=0}^{j+k-1}(1+zQ^a)
 =\prod_{a=0}^{j-1}(1+zQ^a)
       \prod_{a=0}^{k-1}(1+zQ^{j+a}).
 \tag{8}
\]
Divide by \(Q^{j(j-1)/2}\), and in the product on the right choose
degrees \(j-\ell\) and \(\ell\). The remaining power is
\(Q^{\ell^2}\), giving (7) as a polynomial identity, hence at our
root of unity as well.

If \(j+k\ge N\), the numerator \((Q;Q)_{j+k}\) contains
\(1-Q^N\), while both denominator products have length less than
\(N\). Thus this Gaussian binomial coefficient is zero. If
\(j+k<N\), the identity
\({j+k\brack j}_Q=Q^{jk}P_{j+k}/(P_jP_k)\) gives (5).
This proves the theorem for both parities. \(\square\)

There is a second exact expression useful for checking the convention:
\[
                    \Gamma_{jk}=\frac1N[X^D]F_j(X)F_k(X).
 \tag{9}
\]
It follows immediately from (3) and extracts a literal Fourier
coefficient. In particular it verifies the normalization and support
independently of the crossing-matrix calculation.

## 3. Contraction of arbitrary finite words

Let \(A_n=JM^n\), where \(J\) is the original reversal matrix. Put
\[
 (B_3)_{ij}=\begin{cases}\kappa P_{i+j},&i+j<N,\\0,&i+j\ge N,
                    \end{cases}
 \qquad
 (B_4)_{ij}=\begin{cases}\kappa^2N P_{i+j}/(P_iP_j),&i+j<N,\\
                         0,&i+j\ge N.
                    \end{cases}
 \tag{10}
\]
The [original power-three formula](research_traced_three_vertex_endpoint.md)
and [symmetric power-four formula](research_power_four_finite_source.md)
say exactly that
\[
                 V_{n,N}(x,y)=h(x)^TA_nh(y)=f(x)^TB_nf(y),
                      \qquad n\in\{3,4\}.
 \tag{11}
\]
Neither formula deletes a corner or discards repeated-root normals.

**Corollary 2.** For every finite word \(n_1,\ldots,n_m\) with
letters in \(\{3,4\}\),
\[
 h(x)^TA_{n_1}\cdots A_{n_m}h(y)
    =f(x)^TB_{n_1}\Gamma B_{n_2}\Gamma\cdots\Gamma B_{n_m}f(y).
 \tag{12}
\]
There are \(m-1\) matrices \(\Gamma\). All shared Fourier variables
have been integrated over their complete periods. No contour
approximation or asymptotic interchange is used.

*Proof.* Insert \(N\int hh^T=I\) between the original matrices,
substitute (11), and use (4) at each shared boundary. These are finite
sums of entire functions, so the integrations can be performed in any
order. \(\square\)

This also gives ordinary boundary polynomials. Define the invertible
matrix
\[
 S=\operatorname{diag}\left(
           \frac{\kappa^{-1}(-q)^{-j}}{P_j}\right)_{j=0}^{D}M.
 \tag{13}
\]
Then \(f=Sh\), \(\Gamma=SS^T\), and \(A_n=S^TB_nS\).
For the original Newton evaluation vector \(v(w)\), set \(b(w)=Sv(w)\).
Consequently
\[
 v(w_L)^TA_{n_1}\cdots A_{n_m}v(w_R)
       =b(w_L)^TB_{n_1}\Gamma\cdots\Gamma B_{n_m}b(w_R).
 \tag{14}
\]
This is an identity of the entire original boundary polynomials, so
it retains all their derivatives. A cyclic contraction is
\[
 \operatorname{tr}(A_{n_1}\cdots A_{n_m})
       =\operatorname{tr}(B_{n_1}\Gamma\cdots B_{n_m}\Gamma).
 \tag{15}
\]
Equation (15) does not identify an arbitrary cyclic graph with a knot.

## 4. Positive amplitudes and the remaining quadratic phase

For \(0\le j<N\), let
\[
 s_j=\prod_{a=1}^j2\sin(\pi a/N)>0,\qquad
 \delta_j=\exp\!\left(\frac{\pi i j}{2}
                    -\frac{\pi i j(j+1)}{2N}\right).
 \tag{16}
\]
Empty products are one. Directly from \(1-r^a\), one has
\(P_j=\delta_js_j\). On the support of (5) and (10), this gives
\[
 \begin{split}
 \Gamma_{jk}&=\delta_{j+k}^{-1}\frac{s_{j+k}}{s_j^2s_k^2},\\
 \kappa^{-1}(B_3)_{ij}&=\delta_{i+j}s_{i+j},\\
 (\kappa^2N)^{-1}(B_4)_{ij}
      &=q^{-ij}\frac{s_{i+j}}{s_is_j}.
 \end{split}
 \tag{17}
\]
For example, the first equality follows from
\(\delta_{j+k}=\delta_j\delta_kq^{-jk}\), so the factor
\(Q^{jk}\) in (5) is essential.

Expanding (12) or (15) therefore produces positive interior weights
and an explicitly known quadratic oscillation. At each vertex, its
two leg indices \(i,j\) obey \(i+j<N\); at each shared boundary,
its two leg indices \(j,k\) obey \(j+k<N\). After removing the
constant carriers and powers of \(N\), the phase of a cyclic term is
\[
 \sum_{v:n_v=3}\vartheta_N(i_v+j_v)
       -\frac\pi N\sum_{v:n_v=4}i_vj_v
       -\sum_{\{j,k\}\text{ shared}}\vartheta_N(j+k),
 \quad
 \vartheta_N(l)=\frac{\pi l}{2}-\frac{\pi l(l+1)}{2N}.
 \tag{18}
\]
For an open word the boundary factors \(f\), or \(b\), remain in
addition; they need not be positive. Even the cyclic sum is not a sum
of nonnegative terms, because (18) varies with the indices. A lower
bound still requires control of this oscillation. The exact contraction
isolates that issue in a finite quadratic exponential sum with explicit
positive weights; it does not assert the desired lower bound.

The Fourier structure is especially explicit for a cycle. Since
\(\vartheta_N(i+j)=\vartheta_N(i)+\vartheta_N(j)-\pi ij/N\),
all single-leg terms from the three-crossing factors cancel against
their shared-boundary terms. Equation (18) becomes
\[
 \Theta_N=\frac\pi N\sum_{v=1}^m j_v(i_{v+1}-i_v)
       -\sum_{v:n_v=4}\{\vartheta_N(i_v)+\vartheta_N(j_v)\},
                    \qquad i_{m+1}=i_1.
 \tag{19}
\]
The cross term \(e^{\pi ij/N}\) is the kernel of the discrete
Fourier transform on \(2N\) points, before its normalization by
\((2N)^{-1/2}\). A four-crossing vertex adds the displayed diagonal
quadratic phases and the positive factors \(1/(s_is_j)\). This is
an exact Fourier representation, with no limit involved.

The range restrictions and the sine weights remain part of the sum.
They couple the adjacent indices, so Fourier orthogonality cannot
simply erase the cross terms in (19). Plancherel controls a norm of
the resulting weighted transformation; a lower bound for its specified
boundary value or trace still requires an additional argument.

Run `python3 experiments/check_mixed_wire_exact_contraction.py` for
exact polynomial, Fourier-coefficient and original-matrix diagnostics.
The general statements above follow from the written algebraic proof.
