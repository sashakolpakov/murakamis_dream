# Exact spectral coefficient energy at a protected outer face

31 October 2026. **Independently reviewed theorem.** A one-sided original
coefficient with one outer degree zero has an explicit real-spectral
maximum, uniformly through all closed index boundaries and at both level
parities. Its endpoint-conditioned energy is exactly a triangle entropy
in the limit. This is a local coefficient theorem, not a global shared-flow
bound or a new filling theorem.

## 1. The actual coefficient and its positive reference

Put \(d=N-1\), \(m=\lfloor N/2\rfloor\), and

$$
c_r=2\cos\frac{(2r+1)\pi}{N},\qquad
s_r=2\sin\frac{\pi r}{N},\qquad
V_N(\sigma)=\chi_N(\sigma)(\sigma-\Omega_N)^{-1}.
$$

Use the original homogeneous polynomial \(H_{V_N}\). On LEFT support set
\(y=0\) and take

$$
v=(j-i,i,d-j,0),\qquad0\le i\le j<m.
$$

Every dimer vanishes; every lowering step must use \(x\). The original
coefficient has one physical path. Up to its recorded sign,

$$
\left|a_N(v;\sigma)\right|
=\left(\prod_{r=i+1}^j s_r^2\right)
 \left(\prod_{\substack{0\le r<N\\r\notin\{i,\ldots,j\}}}
                         |\sigma-c_r|\right).\tag{1}
$$

All unused rows are present, including the entire omitted half. This is
the exact [triangular-source path formula](actual_global_left_weighted_spectral_envelope.md),
not an absolute replacement inside a recurrence or a division at a node.
The coefficient before absolute values has sign \((-1)^{j-i}\) times the
displayed product with its signed linear factors.

Retain the [positive reference](actual_fejer_odd_regularized_full_numerator.md)

$$
F_N=
\begin{cases}
-V_N(-2),&N\ \text{even},\\
V_N(-2)-N^{-2}V_N'(-2),&N\ \text{odd},
\end{cases}
\qquad
p_N(v)=[x^{v_x}b^{v_b}c^{v_c}y^{v_y}]H_{F_N}>0.\tag{2}
$$

Write \(\mu=i/N\), \(\nu=j/N\), \(w=\nu-\mu\), and define on
\([0,1/2]\)

$$
f(t)=\frac{\Lambda(\pi t)+\Lambda(\pi/2-\pi t)}{\pi},
\qquad f'(t)=\log\cot(\pi t),\qquad f(0)=f(1/2)=0.\tag{3}
$$

The closed triangle entropy is \(C(\alpha)=\sum_r f(\alpha_r)\),
\(\sum_r\alpha_r=1/2\).

## 2. Uniform theorem

Define the exact coefficient supremum

$$
k_N^*(v)=\frac1N\log\max_{\sigma\in[-2,2]}|a_N(v;\sigma)|.
$$

Uniformly over all indices in (1), at both parities,

$$
\begin{aligned}
k_N^*(v)
 &=f(\mu)+f(\nu-\mu)-f(\nu)
                         +O\!\left(\frac{\log N}{N}\right),\\
\frac1N\log p_N(v)
 &=2\bigl(f(\mu)-f(\nu)\bigr)
                         +O\!\left(\frac{\log N}{N}\right).
\end{aligned}\tag{4}
$$

Consequently the exact relative-energy profile is

$$
\boxed{\quad
\frac1N\log
  \frac{\max_{\sigma\in[-2,2]}|a_N(v;\sigma)|^2}{p_N(v)}
=2f(w)+O\!\left(\frac{\log N}{N}\right)
=C(w,\tfrac12-w,0)+O\!\left(\frac{\log N}{N}\right).
\quad}\tag{5}
$$

The constants are independent of \(i,j,N\). The formula includes diagonal
limits, \(\mu=0\), and the limiting upper edge \(\nu=1/2\).
Outer reflection gives \(x=0\); original row reflection gives RIGHT.
Replacing the \(N\)-normalized degrees by \(v/d\) preserves the same
continuous limit.

## 3. Uniform control of the exact product

Set \(\sigma=-2\cos(2\pi\delta)\), \(0\le\delta\le1/2\), and

$$
K(\mu,\nu;\delta)=\int_\mu^\nu
 \log\frac{\sin^2(\pi t)}
 {|\cos^2(\pi t)-\sin^2(\pi\delta)|}\,dt.\tag{6}
$$

Every logarithmic singularity is integrable. We first prove

$$
k_N^*(v)=
\max_{0\le\delta\le1/2}K(\mu,\nu;\delta)
                 +O\!\left(\frac{\log N}{N}\right)\tag{7}
$$

uniformly on the closed index domain.

A contiguous mesh sum of
\(\log|2\sin(\pi(t-a))|\) has upper Riemann error \(O(\log N)\),
uniformly in its shift and interval endpoints. Remove at most two cells
nearest a zero. Their integral is \(O(\log N/N)\), while a sample
exceptionally close to the zero can only improve the upper bound.
On the other cells,
\(\lvert f'(t)\rvert\le C/\operatorname{dist}(t,a+\mathbb Z)\)
gives an accumulated harmonic-sum error \(O(\log N)\).
If every sampled distance to a zero is at least \(c/N\), the same proof
gives a two-sided error. Cosine factors follow by translation.

For \(t_r=(r+1/2)/N\), the unused factors in (1) satisfy

$$
|\sigma-c_r|
=4|\cos(\pi(t_r+\delta))\cos(\pi(t_r-\delta))|.
$$

The integral of this logarithm over \(0\le t\le1\) is zero. Apply the
uniform upper mesh estimate separately to the unused prefix and suffix,
and the sine estimate to the used monomer factors. Their difference is
exactly (6), with only \(O(\log N/N)\) error. No sampled vanishing factor
has been divided out.

For the lower bound in (7), choose a point within \(O(1/N)\) of a
maximizing \(\delta\) on the lattice

$$
\delta_N\in
\begin{cases}
N^{-1}\mathbb Z,&N\ \text{even},\\
N^{-1}(\mathbb Z+\tfrac12),&N\ \text{odd},
\end{cases}
\qquad0\le\delta_N\le\tfrac12.\tag{8}
$$

At these points \(\chi_N(\sigma)=4\), and every sampled cosine stays at
least half a mesh step from its zero. Thus the two-sided estimate applies
to all unused intervals. The modulus of continuity of each logarithmic
integral under an \(O(1/N)\) shift is \(O(\log N/N)\), uniformly in the
interval. This proves (7), including its endpoint cases. Nonempty monomer
products start at \(r\ge1\), so their lower endpoint uses the same elementary
sine estimate.

At even levels (2) is the product (1) at \(\delta=0\). At odd levels
LEFT skips the unique central zero row. The derivative in (2) removes
exactly that factor; its \(N^{-2}\) scalar and the single removed mesh
factor have only \(O(\log N)\) logarithmic cost. Hence, uniformly,

$$
\frac1N\log p_N(v)
=2\int_\mu^\nu\log\tan(\pi t)\,dt
+O\!\left(\frac{\log N}{N}\right)
=2\bigl(f(\mu)-f(\nu)\bigr)
+O\!\left(\frac{\log N}{N}\right).\tag{9}
$$

In particular this is not a comparison with bare odd \(V_N(-2)\), whose
one-sided coefficients vanish.

## 4. The exact maximizing spectral point

For \(0<\mu<\nu<1/2\), differentiation of (6), or of its explicit
logarithmic primitive, gives

$$
\partial_\delta K
=\log\left|
\frac{\cos(\pi(\mu+\delta))\cos(\pi(\nu-\delta))}
{\cos(\pi(\nu+\delta))\cos(\pi(\mu-\delta))}
\right|.\tag{10}
$$

It is positive before the pole interval
\((1/2-\nu,1/2-\mu)\) and negative afterwards. Inside that interval its
sign is the sign of

$$
\cos(\pi(\mu+\nu))
+\cos(\pi(\nu-\mu))\cos(2\pi\delta).
$$

This expression strictly decreases. There is a unique maximum, given by

$$
\boxed{\quad
\cos(2\pi\delta_*)
=-\frac{\cos(\pi(\mu+\nu))}{\cos(\pi(\nu-\mu))}.
\quad}\tag{11}
$$

The quotient has modulus less than one. For \(\mu=0<\nu<1/2\),
the maximum is \(\delta_*=1/2\) and \(K^*=0\); for
\(0<\mu<\nu=1/2\), it is \(\delta_*=0\).
The diagonal interval has zero action. At \(\mu=0,\nu=1/2\) the
maximum need not be unique. Continuity treats all these overlaps.

For an explicit primitive, let
\(J(t)=-\Lambda(\pi t)/\pi\), extended periodically. Then

$$
\begin{aligned}
K(\mu,\nu;\delta)
={}&2[J(\nu)-J(\mu)]\\
&-J(\tfrac12+\nu+\delta)+J(\tfrac12+\mu+\delta)\\
&-J(\tfrac12+\nu-\delta)+J(\tfrac12+\mu-\delta).
\end{aligned}\tag{12}
$$

## 5. Simplification to a triangle entropy

Put \(a=\pi\mu\), \(b=\pi\nu\), \(w=\nu-\mu\).
Equation (11) gives the exact unsquared identities

$$
\begin{aligned}
\cos(2a)+\cos(2\pi\delta_*)&=\sin(2a)\tan(\pi w),\\
\cos(2b)+\cos(2\pi\delta_*)&=-\sin(2b)\tan(\pi w).
\end{aligned}\tag{13}
$$

Let \(h_0=2(f(\mu)-f(\nu))\) and
\(e=2K(\mu,\nu;\delta_*)-h_0\). Directly from (6),

$$
e=2\int_\mu^\nu
\log\left|
\frac{\sin(2\pi t)}
{\cos(2\pi t)+\cos(2\pi\delta_*)}
\right|dt.\tag{14}
$$

The spectral derivative vanishes at the maximizer, so the envelope rule
and (13) yield

$$
\partial_\mu e=-2\log\cot(\pi w),\qquad
\partial_\nu e= 2\log\cot(\pi w).
$$

Thus \(e\) depends only on \(w\), and its zero-width value is zero.
Integrating \(f'(w)=\log\cot(\pi w)\) gives

$$
e=2f(w),\qquad
K^*=f(\mu)+f(w)-f(\nu).\tag{15}
$$

Continuity proves these equalities on the full closed domain. Since
\(f(1/2-w)=f(w)\), equations (7), (9), and (15) prove (4)–(5).

## 6. Global limitation and validation

The limiting LEFT degree vector is
\((w,\mu,1-\nu,0)\). The triangle entropy in (5) is the entropy of the
complete boundary allocation

$$
(w,\tfrac12-w,\tfrac12,0).
$$

This moves \(1/2-\nu\) units from the overloaded middle to the other
middle, while preserving the outer degree. It does **not** preserve the
shared global face targets by itself. On a middle-edge forest, fixing the
other triangle allocations generally fixes the middle transport uniquely.
A global redistribution argument remains necessary before (5) can bound
the [shared conditioned energy](general_endpoint_conditioned_source_energy.md).

Root and an independent peer completed full analytical reviews of the
literal coefficient, both parity grids, uniform logarithmic mesh bounds,
odd derivative, unique spectral maximum, and identity (15): PASS.

The [focused audit](../experiments/audit_actual_protected_outer_spectral_energy.py),
with [results](../experiments/actual_protected_outer_spectral_energy_results.json),
builds the physical coproduct Casimir and extracts coefficients by the
original three-clock inverse DFT. It checks 144 monomer coefficients,
6,408 original grid entries including 2,082 illegal-total zeros, 29
reference coefficients, 21 exact \(\chi_N=4\) samples and 125 node
avoidances, three symbolic identities and six fixed integral identities.
These exact checks supplement the proof; no large-\(N\) rate samples are
used as proof of (4) or of a shared energy bound.

An independent full code review and redirected replay reproduced all counts
at 75 digits, with maximum fixed-identity residual below \(1.8\times10^{-75}\).
The original coefficients are extracted from the physical coproduct, not
constructed from the monomer product being tested.

