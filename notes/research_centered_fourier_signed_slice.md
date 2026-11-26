# A single Fourier sum for the signed Conway blocks

Written research proof, 22 November 2026.

The universal centered Conway tensor has an exact one-sum formula when
one leg is a signed crossing mode. Its entire row energy is then a
positive factorial tail. This gives a uniform exponential norm profile
for every Fourier index, including both endpoints and both parities.
The phases of the individual entries remain in a specified incomplete
Fourier sum. The general three-index tensor is not summed here.

## 1. Original matrices and phase conventions

Keep the full original Hermite algebra and centered basis of the
Fourier compiler. Put
\[
 d=N-1,\quad N\ge2,\quad q=e^{\pi i/N},\quad Q=q^2,\quad
 \kappa=q^{d^2/2},\quad F_r=(Q;Q)_r,\quad
 S_r=|F_r|=\prod_{j=1}^r2\sin(\pi j/N).
 \tag{1}
\]
Empty products are one. All \(F_r\), \(0\le r\le d\), are nonzero
and \(F_d=N\). For \(0\le a\le d\), define
\[
 k_a=a-d/2,\qquad
 \lambda_a=e^{2\pi i k_a/N}=-qQ^a,\qquad
 \gamma_a=e^{-\pi i k_ad/N},\qquad
 U_{ra}=N^{-1/2}\gamma_a\lambda_a^r .
 \tag{2}
\]
The displayed exponentials fix the half-integer phases at even levels;
fractional powers of the numerical value \(-q\) are not used.

The centered vectors satisfy \(f_a=\sum_rU_{ra}e_r\),
\(\phi(f_af_b)=\delta_{ab}\), \(R^+=\sqrt N f_0\), and
\(R^-=\sqrt N f_d\). Write
\[
 C_{abc}=\phi(f_af_bf_c),\qquad
 \omega_b=N^{-1/2}e^{\pi i k_bd/N}=\phi(f_b).
 \tag{3}
\]
Thus, if \(T^+\) is multiplication by \(R^+\) in Newton coordinates,
\((U^*T^+U)_{cb}=\sqrt N C_{0bc}\).
The original full-channel matrix in the covariance source is
\[
 T^+_{ij}=\kappa(-1)^i q^{i+j^2}{i\brack j}_Q
 \quad(0\le j\le i\le d),\qquad T^-=\overline{T^+}.
 \tag{4}
\]
The Gaussian binomial is \(F_i/(F_jF_{i-j})\).
Equation (4) is a matrix on all \(N\) Newton coordinates, including
the repeated-root normal directions.

We will use the exact reflection identities
\[
 F_hF_{d-h}=N(-1)^hQ^{h(h+1)/2},\qquad
                         S_hS_{d-h}=N.
 \tag{5}
\]
Indeed \(F_d/F_{d-h}=\prod_{j=1}^h(1-Q^{-j})
=(-1)^hQ^{-h(h+1)/2}F_h\).

## 2. A finite root-of-unity summation

For \(0\le j\le d\) the following polynomial identity holds:
\[
 \sum_{i=j}^d {i\brack j}_Q x^{i-j}
                    =(xQ^{j+1};Q)_{d-j}.
 \tag{6}
\]
Here is a finite coefficient proof. The coefficient of \(x^n\) in
\(\prod_{r=0}^j(1-Q^rx)^{-1}\) is \({j+n\brack j}_Q\) for
\(0\le n\le d-j\). This follows inductively from multiplying by
\(1-Q^jx\): the coefficient recursion is the finite Pascal identity
\({j+n\brack j}_Q={j+n-1\brack j-1}_Q
                 +Q^j{j+n-1\brack j}_Q\).
On the other hand,
\[
 \prod_{r=0}^j(1-Q^rx)^{-1}
       =\frac{(xQ^{j+1};Q)_{d-j}}{1-x^N}.
\]
In degrees at most \(d-j<N\), the denominator contributes only its
constant term. The numerator already has that degree, proving (6).
Only factorial indices below \(N\) enter this argument.

In particular, evaluating the polynomial at \(x=Q^{-c}\) gives
\[
 \sum_{i=j}^d{i\brack j}_QQ^{-ci}
 =\begin{cases}
 0,&j<c,\\
 Q^{-cj}F_{d-c}/F_{j-c},&j\ge c.
 \end{cases}
 \tag{7}
\]
For \(j<c\), the product in (6) contains \(1-Q^0\). For \(j\ge c\)
its consecutive factors have exponents \(j+1-c,\ldots,d-c\).
Thus (7) includes \(j=c\), \(c=0\), and \(c=d\) without a limiting
interpretation.

## 3. The signed slice in one finite Fourier sum

The exact answer for the positive signed slice is
\[
 \boxed{\quad
 C_{0bc}=
 \frac{\kappa\,\overline{\gamma_c}\gamma_b}{N^{5/2}}\,
 F_{d-c}q^{-c^2}\lambda_b^cQ^{bd}
                     \sum_{r=c}^d F_rQ^{-br}.
 \quad}
 \tag{8}
\]
Every factor and endpoint is specified; no infinite completion is used.

To derive it, insert (2) and (4) in \(U^*T^+U\).
Since \((-q)^i\lambda_c^{-i}=Q^{-ci}\), the result is
\[
 (U^*T^+U)_{cb}
 =\frac{\kappa\overline{\gamma_c}\gamma_b}{N}
   \sum_{j=0}^d q^{j^2}\lambda_b^j
                       \sum_{i=j}^d{i\brack j}_QQ^{-ci}.
 \tag{9}
\]
Apply (7), and set \(j=c+h\). The remaining expression is
\[
 \frac{\kappa\overline{\gamma_c}\gamma_b}{N}
 F_{d-c}q^{-c^2}\lambda_b^c
 \sum_{h=0}^{d-c}
       \frac{(-1)^hQ^{h(h-1)/2+(b+1)h}}{F_h}.
 \tag{10}
\]
Use (5) in each term of this last finite sum:
\[
 \frac{(-1)^hQ^{h(h-1)/2+(b+1)h}}{F_h}
                         =\frac1N F_{d-h}Q^{bh}.
 \tag{11}
\]
Changing \(r=d-h\) gives \(Q^{bd}N^{-1}\sum_{r=c}^dF_rQ^{-br}\).
Finally divide (9) by \(\sqrt N\), proving (8).
The two Fourier indices have not been interchanged: \(b\) is the
input matrix index and \(c\) the output index. Symmetry
\(C_{0bc}=C_{0cb}\) is also guaranteed by its original Frobenius
definition, even though (8) displays the indices asymmetrically.

There are useful exact endpoint checks. Since \(\gamma_0=\kappa\),
\[
 C_{0b0}=N^{-3/2}\gamma_bQ^{bd}
                        \sum_{r=0}^dF_rQ^{-br},\qquad
 C_{000}=\kappa N^{-3/2}\sum_{r=0}^dF_r.
 \tag{12}
\]
At the other endpoint, (8) simplifies to
\[
                              C_{0bd}=\omega_b/N.
 \tag{13}
\]
This is required by \(f_0f_d=R^+R^-/N=1/N\); the original closing
row has not been replaced. For \(N=2\), \(q=i\) and
\(\kappa=e^{\pi i/4}\), and the complete slice is
\[
 (C_{0bc})_{b,c=0}^1
     =\frac1{2\sqrt2}
       \begin{pmatrix}3\kappa&\kappa^{-1}\\
                       \kappa^{-1}&\kappa\end{pmatrix}.
 \tag{14}
\]
Thus the smallest level uses the same formula and phases.

### 3.1 Exact transport of the remaining phase

The tail in (8) has a first-order polynomial equation, with its
lower-end forcing retained. Define
\[
 \mathcal S_c(x)=\sum_{r=c}^dF_rx^r.
\]
Then
\[
 \boxed{\qquad
 (1-x)\mathcal S_c(x)+Qx\mathcal S_c(Qx)=F_cx^c.
 \qquad}
 \tag{14a}
\]
Indeed the coefficient at \(x^c\) is \(F_c\). Every subsequent
coefficient through \(x^d\) is
\(F_r-(1-Q^r)F_{r-1}=0\); the possible coefficient at \(x^N\)
vanishes because \(Q^N=1\). No infinite tail is appended.

On the cyclic Fourier grid put \(g_b=\mathcal S_c(Q^{-b})\),
with \(b\) read modulo \(N\). Equation (14a) becomes
\[
 (1-Q^{-b})g_b+Q^{1-b}g_{b-1}=F_cQ^{-bc}.
 \tag{14b}
\]
This is phase-retaining boundary transport for the exact sum in (8).
At \(b=0\) it says \(g_{N-1}=F_c/Q\); one must not divide by
\(1-Q^{-b}\) there. This equation followed by \(b=N-1,\ldots,1\)
determines all the other values, since the coefficient \(Q^{1-b}\)
never vanishes. No bounded inverse or individual-entry asymptotic is
inferred from this uniqueness.

## 4. An exact positive energy for every index

Define \(E_c^+=\sum_{b=0}^d|C_{0bc}|^2\). Finite Fourier
orthogonality in (8), followed by (5), gives
\[
 \boxed{\qquad
 E_c^+=\frac{|F_{d-c}|^2}{N^4}\sum_{r=c}^d|F_r|^2
       =\frac1{N^2S_c^2}\sum_{r=c}^dS_r^2.
 \qquad}
 \tag{15}
\]
Explicitly,
\(\sum_b|\sum_{r=c}^dF_rQ^{-br}|^2
       =N\sum_{r=c}^d|F_r|^2\).
All other \(b\)-dependent factors in (8) have modulus one.
This sums the actual coherent entries before removing their phases.
It is a row or column energy of this symmetric slice, not the
absolute sum of the original multiplication paths.
The endpoints are
\[
 E_0^+=N^{-2}\sum_{r=0}^dS_r^2,\qquad E_d^+=N^{-2}.
 \tag{16}
\]

For the negative signed slice the compiler's conjugation rule gives
\[
 C_{dbc}=\overline{C_{0,d-b,d-c}},\qquad
             E_c^-:=\sum_b|C_{dbc}|^2=E_{d-c}^+.
 \tag{17}
\]
These identities keep the original signed crossings and their carriers.

## 5. Uniform exponential profile, including the endpoints

Put
\[
 J(t)=\int_0^t\log(2\sin\pi u)\,du,\qquad
 A=J(5/6)>0,\qquad
 \Psi(t)=
 \begin{cases}A-J(t),&0\le t\le5/6,\\0,&5/6\le t\le1.\end{cases}
 \tag{18}
\]
Then, uniformly for all \(c=0,\ldots,d\),
\[
 \boxed{\qquad
 \log\sqrt{E_c^+}=N\Psi(c/N)+O(\log N),\qquad
 \log\sqrt{E_c^-}=N\Psi((d-c)/N)+O(\log N).
 \qquad}
 \tag{19}
\]
The second argument can be replaced by \(1-c/N\) with the same error.

The endpoint-uniform factorial estimate from the covariance proof is
\(\log S_r=NJ(r/N)+O(\log N)\), uniformly \(0\le r<N\).
Taking the largest term in the positive sum (15), then bounding the
sum by \(N\) times that term, proves
\[
 \log\sqrt{E_c^+}
   =N\left\{\max_{c\le r\le d}J(r/N)-J(c/N)\right\}+O(\log N).
 \tag{20}
\]
The integral of \(|\log(2\sin\pi u)|\) over an interval of length
\(1/N\) is \(O(\log N/N)\), uniformly including either endpoint.
Thus the discrete maximum differs from
\(\max_{x\in[c/N,1]}J(x)\) by that amount.

The derivative \(J'(t)=\log(2\sin\pi t)\) changes sign only at
\(1/6,5/6\). Also \(J(1)=0\) and \(J(1-t)=-J(t)\).
These follow from sine reflection and the full factorial product;
equivalently the endpoint-uniform estimate at \(r=d\), where
\(S_d=N\), gives \(J(1)=0\).
Consequently that continuous maximum is \(A\) up to \(t=5/6\),
and is \(J(t)\) afterward. This proves (19).
The same interval estimate justifies the one-mesh replacement in its
negative version.

In particular \(\max_t\Psi(t)=2A\), attained at \(t=1/6\), and
\[
              \log\max_{b,c}|C_{0bc}|=2AN+O(\log N).
 \tag{21}
\]
Indeed a row's largest entry lies between its Euclidean norm divided
by \(\sqrt N\) and that norm. The negative slice has the same maximum.
No particular individual entry is assigned a lower rate by (19).

## 6. Scope and complete sources

This collapses the two-index Fourier calculation of each signed
crossing multiplication block to one incomplete factorial Fourier sum.
It gives its exact row energies and their uniform rates.
It does not collapse arbitrary \(C_{abc}\) to a product or bounded
number of summands. Nor does it estimate the oscillatory tail in (8)
at every pair of indices, give a geometric metric for the full tensor,
or control its coherent contraction with a short component.

All norms here are the centered Fourier norm, unitarily equivalent
to the positive Newton coefficient norm. They are not identified with
a physical Hilbert--Schmidt metric or the original scalar closing.
The \(N\) coordinates and the exact matrix (4) retain every original
Hermite normal; no distinct-root quotient or parity restriction enters.
There is no new volume estimate or finite-exception conclusion.

The complete proof texts used are:

| Source | SHA-256 |
|---|---|
| [Centered Fourier compiler, 405 lines](research_centered_fourier_conway_compiler.md) | 0edbabe42280d70e4d5dcbcb55b188a3e773c14b99fbd212eb0fe8c5b176a413 |
| [Actual crossing covariance, 415 lines](research_actual_newton_crossing_gaussian_covariance.md) | ce2b1b8efbbcffa8bafe0d0de4f7ce12febf193e433d8e3291f7d2a8c826fa3f |

The finite summation, phase bookkeeping and energy calculation are
proved above. No generic-parameter orthogonality or root-specialization
of a positive measure is imported. Earlier source notes remain unchanged.

For definition-only coverage,
\(\mathcal S_0(1)=\sum_{r=0}^{N-1}(Q;Q)_r\) is the root value of the
Kontsevich series \(\sum_{r\ge0}(u;u)_r\) discussed in the introduction
of [Zagier (2001)](https://people.mpim-bonn.mpg.de/zagier/files/doi/10.1016/S0040-9383%2800%2900005-7/fulltext.pdf).
At \(u=Q\), every term with \(r\ge N\) is zero, so this identification
is literal. No modular identity, radial limit or asymptotic from that
paper is used in the proof.
