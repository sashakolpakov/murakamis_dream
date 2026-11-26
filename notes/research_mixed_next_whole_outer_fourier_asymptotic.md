# A nonzero asymptotic for the whole outer Fourier observation

Private research theorem, 9 November 2026. This assembles the local
Gaussian calculation and the estimates of every remaining part of
the exact finite observation. The reflected full-source bound supplies
the hypothesis that was still open in the negative-contour criterion.
The conclusion concerns one specified short-tangle source. It does
not establish its comparison with the adjoining outgoing source or
stability under arbitrary short partial fillings.

## 1. The finite observation

Use the original Newton polynomials \(e_j\), crossing \(R_N\), and
full Hermite functional \(\phi_N\), with precisely the conventions
in [the local Gaussian theorem](research_mixed_next_outer_local_gaussian_and_remaining_currents.md),
equations (1)--(3). Thus
\[
 D=N-1,\qquad M=\lceil N/2\rceil,\qquad U=\lfloor N/2\rfloor-1,
 \qquad C_{N,3}=\exp(3\pi iD^2/(4N)),
\]
\[
 K_N(x,y)=\sum_{j=0}^{D}e_j(x)e_j(y),\qquad
 Q_N^{\rm full}(u)=
 \phi_N^{(x)}[R_N(x)^3 K_N(-2,x)K_N(x,-2\cos u)].
\]
Let \(\widehat Q_N^{\rm full}\) denote this ordinary polynomial in
the spectral variable \(y=-2\cos u\). With \(T_k\) the Chebyshev
polynomial specified by \(T_k(\cos u)=\cos(ku)\), define
\[
 \mathcal O_{N,k}
  =\phi_N[R_N^3e_M\widehat Q_N^{\rm full}T_k(-\,\cdot/2)],
 \qquad \delta=\frac12-\frac{k}{N},\qquad 0\le k\le U.
 \tag{1}
\]
This is the full finite observation, including the original first
normal terms and the odd simple node. The exact low-edge identity
licenses using the shortened source on its sampling contour; no
identity between distinct off-grid kernels is assumed.

Let \(S(u)\) be the original calibrated inner action, and let
\(u_\delta=\beta_\delta-iK_\delta\) be the selected stationary point
of
\[
 \Psi_\delta(u)=S(u)+\frac{3iu^2}{4\pi}-i\delta u.
\]
Write
\[
 \mathcal S(\delta)=\Psi_\delta(u_\delta),\qquad
 \Gamma(\delta)=\Re\mathcal S(\delta).
 \tag{2}
\]
Let \(\mathcal A(u)\) be the nonzero inner Gaussian coefficient
defined by equation (5) of the local Gaussian theorem.

## 2. Statement

**Theorem.** Fix \(0<\delta_1\le1/2\). Uniformly over all the
integer frequencies in (1) satisfying
\(\delta\in[\delta_1,1/2]\), at both parities and all sufficiently
large \(N\),
\[
 \mathcal O_{N,k}
   =N^{-1}B_{N,k}e^{N\mathcal S(\delta)}
                  \{1+O(N^{-1})\},
 \qquad 0<c_{\delta_1}\le |B_{N,k}|\le C_{\delta_1}.
 \tag{3}
\]
The original coefficient is
\[
 B_{N,k}=
 \frac{\chi_N C_{N,3}^{\,2}}{2\sqrt{2\pi}}\,
 \frac{a^{\rm par}(u_\delta)\mathcal A(u_\delta)
                    (1+e^{-2iku_\delta})}
      {\sqrt{-\Psi_\delta''(u_\delta)}},
 \tag{4}
\]
where the square root has positive real part, and
\[
 \chi_N=\begin{cases}i,&N\text{ even},\\-1,&N\text{ odd},\end{cases}
 \qquad
 a^{\rm par}(u)=
 \begin{cases}\sin u,&N\text{ even},\\
 \sin u\,\sin(u/2),&N\text{ odd}.
 \end{cases}
\]
In particular the whole observation is nonzero for all sufficiently
large levels in this range, and
\[
 \frac1N\log|\mathcal O_{N,k}|
    =\Gamma\!\left(\frac12-\frac{k}{N}\right)
          +O\!\left(\frac{\log N}{N}\right)
 \tag{5}
\]
uniformly there.

The constants may depend on \(\delta_1\). This theorem does not
assert uniformity as \(\delta\) tends to zero. Zero cosine frequency,
\(k=0\), is included: it has \(\delta=1/2\) and the reflected factor
in (4) is exactly two.

## 3. Proof

The [reflected full-source theorem](research_mixed_next_reflected_rectangle_full_inner_bound.md)
proves, for every fixed \(\tau>0\),
\[
 |Q_N^{\rm sh}(a+ih)|
 \le C_\tau
  \exp N\{\max(\Re S(a+ih),17/10)+\tau\},
 \quad 0\le a\le4/3,\quad0\le h\le2/5.
 \tag{6}
\]
Its source is exactly the shortened-output, full-inner-trace source
used in [the negative-contour criterion](research_mixed_next_outer_negative_contour_criterion.md).
The rectangle, phase normalization, parity quantifiers, and allowance
\(\tau\) in (6) are exactly those of hypothesis (H) there.

That criterion therefore applies unconditionally. Together with
the positive-contour and physical-tail estimates, it gives
\[
 \mathcal O_{N,k}
   =G_{N,k}+O(e^{N(\Gamma(\delta)-\eta)})
 \tag{7}
\]
for some \(\eta>0\) depending only on the fixed frequency interval.
Here \(G_{N,k}\) is the actual local integral in the exact contour
decomposition, with its original scalar and reflected multiplier.
All other contour pieces, sampling corrections, and removed physical
nodes are included in the remainder.

Equation (18) of the local Gaussian theorem gives (3)--(4) for
\(G_{N,k}\), including the two uniform bounds on the coefficient.
Relative to its size \(N^{-1}e^{N\Gamma(\delta)}\), the error in
(7) is \(O(Ne^{-N\eta})\). It is absorbed in the existing
\(O(N^{-1})\) relative error. This proves (3). Taking absolute
values and logarithms proves (5). \(\square\)

## 4. What this settles

For this exact observation, existence of the geometric stationary
point has now been supplemented by the required nonzero coefficient
and control of all competing terms. No positivity of the signed
quantum sum is assumed. The proof uses the original finite contour
identity, a local Gaussian expansion, and absolute estimates on the
remaining contour.

The subsequent contraction with the outgoing coefficients is a
different finite sum. Its required comparison with the geometric
rate \(\Lambda\) remains open. This theorem is not a proof of the
volume conjecture for a new family of knots or of cofiniteness under
arbitrary short partial fillings.

## Source versions

- Local Gaussian with its original nonzero coefficient:
  6f2b155eee54cfd8a930d9af146ab96c3de277aac70d2de51b5f8318523f45ab.
- Exact negative-contour reduction and sufficient implication:
  ae0bbd44353baa5f6679d9c3b7ea3d61f40490dcdfdf7837f505c45dd75ea99a.
- Full reflected source bound discharging that hypothesis:
  577fa285f774b4eb93cd2a995f22faff6d0b7f72c20e375b95db57c690ecf85f.

No mathematical numerical evaluation is used in this assembly.
