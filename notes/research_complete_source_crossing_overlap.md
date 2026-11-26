# How much a crossing changes the complete-color vector

Research proof, 3 November 2026. The frozen manuscripts are unchanged.

A vector concentrated near the complete color need not be almost
invariant under a fixed crossing. Here that question can be answered
for the original vector, without choosing an artificial test vector.
Its normalized matrix coefficient has a Gaussian limit. A crossing
step of size \(1/N\) changes the vector by \(O(1/N)\), but \(N\)
such steps produce a change of fixed positive size. This distinguishes
an infinitesimal estimate from the estimate needed for a fixed knot.

## 1. The vector and the norm

For an integer level \(N\ge2\), put \(L=\lfloor(N-1)/2\rfloor\) and
\[
 c_a=2\cos((2a+1)\pi/N),\qquad
 \tau_a=\pi-(2a+1)\pi/N,\qquad 0\le a\le L.
 \tag{1}
\]
These are the distinct physical nodes. In particular, the odd-level
list includes \(c_L=-2\), with \(\tau_L=0\). Define
\[
 S_j=\prod_{k=1}^j2\sin(k\pi/N),\qquad
 e_j(z)=S_j^{-2}\prod_{k=0}^{j-1}(c_k-z),\qquad
 F_{N,a}=\sum_{j=0}^{N-1}e_j(c_a)e_j(-2).
 \tag{2}
\]
Empty products are one. The original Newton polynomial \(e_j(c_a)\)
vanishes when \(j>a\). Thus (2) is a sum of strictly positive terms
for \(0\le j\le a\), and it is also the value of the original
complete-end kernel \(K_N(\tau_a,0)\).

We use the ordinary Euclidean norm on these distinct values, with
each value counted once. No first derivatives or trace weights are
included in this norm. Set
\[
 (U_{t,N}v)_a=\exp\!\left(\frac{itN\tau_a^2}{4\pi}\right)v_a,
 \qquad t\in\mathbb R.
 \tag{3}
\]
This is the unitary part of the crossing action on physical values.
It is not a claim that the full action on values and first derivatives
is unitary. A common scalar of modulus one does not affect the
distance minimized over scalar phases below.

**Theorem 1.** Write \(M_\infty=4G/\pi\), where \(G\) is Catalan's
constant. At both level parities,
\[
 \|F_N\|_2^2=
 \frac{e^{2NM_\infty}}{32\sqrt2\,N^{5/2}}
                 \bigl(1+O(N^{-1/2})\bigr).
 \tag{4}
\]
For every fixed compact interval of real \(t\), uniformly on that
interval,
\[
 \frac{\langle F_N,U_{t,N}F_N\rangle}{\|F_N\|_2^2}
       =(1-it/2)^{-1/2}+O(N^{-1/2}).
 \tag{5}
\]
The inner product is conjugate-linear in its first argument. The
square root in (5) is the continuous branch equal to one at zero.
Consequently, for every fixed \(t\ne0\),
\[
 \lim_{N\to\infty}\min_{|\omega|=1}
 \frac{\|U_{t,N}F_N-\omega F_N\|_2}{\|F_N\|_2}
 =\sqrt{2-2(1+t^2/4)^{-1/4}}>0.
 \tag{6}
\]
On the other hand,
\[
 \frac{\|(U_{1/N,N}-I)F_N\|_2}{\|F_N\|_2}
       =\frac{\sqrt3}{4N}\bigl(1+O(N^{-1/2})\bigr).
 \tag{7}
\]

## 2. Proof from the original kernel

The [thin complete-kernel theorem](research_bare_kernel_thin_rectangle.md)
gives, on a fixed neighborhood of \(\tau=0\),
\[
 K_N(\tau,0)=N^{-3/2}a(\tau)e^{N\Psi(\tau)}(1+O(N^{-1})),
 \quad
 a(0)=\tfrac14,\quad
 \Psi(\tau)=M_\infty-\frac{\tau^2}{4\pi}+O(\tau^4).
 \tag{8}
\]
Both \(a\) and \(\Psi\) are even and holomorphic there. The
expansion is uniform at both parities, including real angles of
size \(N^{-1/2}\). For every fixed small \(b>0\), the direct
[real-period estimate](research_complete_source_pick_observation.md#2-two-existing-bounds-for-the-complete-factor)
also gives a strict exponential loss when \(b\le\tau\le\pi\).
At every physical node the full and low complete kernels agree,
so that estimate applies to \(F_{N,a}\). Thus no part of the
physical-value vector is being omitted in the following calculation.

Put \(x_a=\sqrt N\,\tau_a\). For \(0\le\tau_a\le b\), (8)
gives a Gaussian upper bound and the local expansion
\[
 |F_{N,a}|^2=
 \frac{e^{2NM_\infty}}{16N^3}
 e^{-x_a^2/(2\pi)}
 \left(1+O\!\left(\frac{1+x_a^2+x_a^4}{N}\right)\right)
 \tag{9}
\]
on every growing window \(x_a\le N^{1/10}\). The rest of this
small-angle interval is bounded by \(C N^{-3}e^{2NM_\infty-cx_a^2}\).
The portion with \(\tau_a\ge b\) has an exponential gap.
This justifies summation of (9), also after multiplication by any
fixed power of \(x_a\), or by \(e^{itx_a^2/(4\pi)}\) with \(t\)
in a fixed compact real interval.

In increasing order, the \(x_a\) form a half-line grid of spacing
\(h_N=2\pi/\sqrt N\), with offset \(h_N/2\) at even levels
and zero at odd levels. For a continuously differentiable integrable
function \(f\) with integrable derivative, either Riemann sum
satisfies
\[
 h_N\sum_a f(x_a)=\int_0^\infty f(x)\,dx+O(h_N).
 \tag{10}
\]
The finite physical endpoint can be replaced by infinity here with
an exponentially small error. The elementary cellwise estimate
\(h_N\int|f'|\), with a possible initial interval of length \(h_N\),
proves (10). It is uniform for the Gaussian functions just used.
In particular, the single complete node at odd level has relative
mass \(O(N^{-1/2})\); it does not alter the limiting integral.

The two required integrals are
\[
 \int_0^\infty e^{-x^2/(2\pi)}\,dx=\frac{\pi}{\sqrt2},
 \qquad
 \frac{\int_0^\infty e^{-(1-it/2)x^2/(2\pi)}\,dx}
      {\int_0^\infty e^{-x^2/(2\pi)}\,dx}
       =(1-it/2)^{-1/2}.
 \tag{11}
\]
Equations (9)--(11) prove (4) and (5), including their normalization.
For two vectors of equal norm, minimizing their squared distance
over a scalar phase gives twice that norm squared minus twice the
absolute inner product. Applying this identity to (5) proves (6).

For (7), write \(T_{N,a}=x_a^2/(4\pi)\). The same Riemann sums
with polynomial factors give
\[
 \frac{\sum_a T_{N,a}^2|F_{N,a}|^2}{\|F_N\|_2^2}
          =\frac3{16}+O(N^{-1/2}),\qquad
 \frac{\sum_a T_{N,a}^4|F_{N,a}|^2}{\|F_N\|_2^2}=O(1).
 \tag{12}
\]
Now use \(2-2\cos y=y^2+O(y^4)\) in the exact squared distance
for \(U_{1/N,N}\). This proves (7).

## 3. What a representation-theoretic lower bound would need

An elementary spectral-gap argument explains what additional data
would make almost-invariance useful. Let \(A_N\ge0\) be a positive
operator with one-dimensional kernel spanned by a unit vector \(g_N\),
and suppose
\[
 A_N\succeq\gamma_N(I-P_N),\qquad
 \langle v_N,A_Nv_N\rangle\le
          \varepsilon_N^2\gamma_N\|v_N\|^2,
 \quad 0\le\varepsilon_N<1,
 \tag{13}
\]
where \(P_N\) projects onto \(g_N\). Then
\(\|(I-P_N)v_N\|\le\varepsilon_N\|v_N\|\).
For a specified bounded linear closing functional \(\ell_N\),
orthogonal decomposition and the triangle inequality give
\[
 |\ell_N(v_N)|\ge
 \left(|\ell_N(g_N)|\sqrt{1-\varepsilon_N^2}
             -\|\ell_N\|\varepsilon_N\right)\|v_N\|.
 \tag{14}
\]
The factor in parentheses must be positive and quantitatively
controlled. A small residual alone cannot guarantee this: the
closing functional might vanish on the invariant line.

For unitary generators one can take
\(A_N=\sum_s w_s(U_s-I)^*(U_s-I)\), with \(w_s>0\).
The use of spectral gaps to estimate distance from invariant vectors
is standard; see Bekka, de la Harpe, and Valette,
[*Kazhdan's Property (T)*, Chapter 1](https://www.cambridge.org/core/books/abs/kazhdans-property-t/definitions-first-consequences-and-basic-examples/21A0D7F3B446FB0607DA14F1479F7394).
Equations (13)--(14) have been proved directly above; no property
\((T)\) assertion for the present crossing operators is assumed.

For the source in this note, (6) rules out almost-invariance under
any fixed nonzero \(U_t\) in the stated norm. Equation (7) explains
why a small step does not resolve that obstruction: after \(N\)
steps, \(U_{1/N,N}^N=U_{1,N}\), and the defect in (6) is positive.
The separate [positive observation estimate](research_complete_source_pick_observation.md)
computes the smaller rate measured by a particular fixed-time
observation operator. For every fixed real \(n\ge3\), its
Corollary 3 and (4) above give
\[
 \frac{F_N^*H_{n,N}F_N}{\|F_N\|^2}
  =32\sqrt2\,C_n\,N^{1/2}
       e^{-2N(M_\infty-M_n)}(1+O(N^{-1/2})),
 \qquad C_n>0,\quad M_n<M_\infty .
\]
The strict action difference is
\(M_\infty-M_n=\int_0^{1/2}H_n(\chi)\,d\chi>0\).
Consequently the least eigenvalue of this positive operator
is no larger than the displayed Rayleigh quotient. This
particular operator does not have a polynomial lower bound
on the entire physical-value space. Its small value on
\(F_N\) is not invariance under the crossing unitaries.

The proved [local geometric Gaussian estimate](research_internal_pair_local_gaussian.md#7-the-explicit-local-packet-with-two-free-outside-colors)
does supply a nonzero norm and a small annihilation residual after
the geometric phase is removed and the variables are rescaled.
To use (14) for the full finite quantum sum still requires the
actual closing functional and a bound on the complementary contour.
Neither (5) nor (14) asserts the missing global lower bound.

## 4. Reproduction

Run the [focused checker](../experiments/check_complete_source_crossing_overlap.py):

~~~sh
python3 experiments/check_complete_source_crossing_overlap.py
~~~

It checks the Gaussian constants and the exact finite-vector
identities at both parities. Its convergence table is diagnostic;
the uniform asymptotic and the passage through both parities are
proved above. The [record](../repro/results/research-complete-source-crossing-overlap.json)
stores the input hashes and separates those two kinds of check.
