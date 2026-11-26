# The complete transfer near its geometric outgoing coordinate

Private research assembly, 9 November 2026. The finite transfer has
its original nonzero geometric asymptotic on a fixed complex
neighborhood of the outgoing coordinate. The incoming ordinary
color remains fixed at \(-2\). The neighborhood and every contour
are chosen before the level tends to infinity.

## 1. The finite sum and the geometric action

Fix an actual complete word in powers three and four, beginning
\(343\), of length at least five. Let \(z_*\) be its original
third outgoing coordinate. Put
\[
 D=N-1,\qquad r=e^{-2\pi i/N},\qquad P_b=(r;r)_b,
 \qquad Z=e^{-2\pi iz}.
 \tag{1}
\]
Retain the original prefix polynomial \(F_{34,N}(w,Y)\) and kernel
\[
 C_{0,N}(Y,Z)=
 \sum_{j=0}^{D}
 \frac{Y^{-j}(rY;r)_j(rZ;r)_j}{(r;r)_j^2}.
 \tag{2}
\]
The transfer is the entire original finite sum
\[
 T_N(z)=\sum_{b=0}^{D}
       \frac{F_{34,N}(-2,r^b)}{P_b}C_{0,N}(r^b,e^{-2\pi iz}).
 \tag{3}
\]
In its coefficient representation it contains both original
Fourier sectors. No physical row is removed from (3).

Let
\[
 P(z)=\mathcal P_0^+(-2,z),\qquad A(z)=\mathcal A_0(-2,z)
 \tag{4}
\]
be the action and coefficient of the original local-source theorem.
Their additive constant, factorial symbols and determinant branch
are unchanged. Both are holomorphic near \(z_*\), and
\(A(z_*)\ne0\).

**Theorem.** There is a fixed disk \(V\) about \(z_*\) such that,
at both parities and all sufficiently large levels,
\[
 T_N(z)=N^{-2}A(z)e^{NP(z)}\{1+\varepsilon_N(z)\},
 \qquad
 \sup_V|\varepsilon_N|\le C/N.
 \tag{5}
\]
The error is holomorphic. On every fixed smaller disk and for
every fixed \(j\ge0\),
\[
 \sup|\partial_z^j\varepsilon_N|\le C_j/N.
 \tag{6}
\]
After shrinking \(V\), the coefficient \(A\) is bounded away
from zero there. Thus \(T_N\) has no zeros on that disk for all
sufficiently large levels, and uniformly on smaller disks
\[
 \frac1N\log|T_N(z)|=\Re P(z)+O(\log N/N).
 \tag{7}
\]

## 2. Proof with the exact remainder retained

Let \(I_N(w,z)\) be the original fixed-path local integral, including
its full finite prefix, forced weight and following kernel. Put
\[
 \begin{split}
 R_N^+(w,Z)&=\sum_{b=\lceil N/2\rceil}^{D}
            \frac{F_{34,N}(w,r^b)}{P_b}C_{0,N}(r^b,Z),\\
 E_N^-(w,z)&=\mathcal T_N(w,e^{-2\pi iz})
                         -I_N(w,z)-R_N^+(w,e^{-2\pi iz}).
 \end{split}
 \tag{8}
\]
These definitions give an exact identity at every level.
The [left-remainder theorem](research_mixed_next_left_remainder_complex_extension.md)
proves on a fixed complex neighborhood of \((-2,z_*)\)
\[
 |e^{-N\mathcal P_0^+(w,z)}E_N^-(w,z)|\le Ce^{-\eta N}
 \qquad(\eta>0).
 \tag{9}
\]
Its proof keeps the exact local integral. In particular, its
exponentially small error does not include the algebraic error
of a stationary-phase expansion.

The [physical action anchor](research_mixed_next_physical_half_input_action_anchor.md)
and [endpoint-dominance theorem](research_mixed_next_positive_transition_endpoint_dominance.md)
give the full combined-frequency gap
\[
 \mathcal D(t,Z_*)+\Gamma(1/2-t)
 \le \Re P(z_*)-\gamma,\qquad
 \gamma=\frac1{2\cdot10^{13}},\quad 0\le t\le1/2.
 \tag{10}
\]
Here \(Z_*=e^{-2\pi iz_*}\). This is precisely hypothesis (8)
of the [outgoing boundary-extension proposition](research_mixed_next_attachment_boundary_extension_scope.md).
That proposition, with the original finite outgoing coefficients,
proves on a fixed disk
\[
 |e^{-NP(z)}R_N^+(-2,e^{-2\pi iz})|
                      \le Ce^{-\gamma N/2}.
 \tag{11}
\]
The first step of that proposition supplies a bound uniform over
all outgoing rows, including the terminal row. The last frequency
range uses continuity of the rate and a whole-frequency upper
bound. It does not require a relative Fourier asymptotic as the
frequency parameter tends to zero.

The [original local-source theorem](research_mixed_three_four_next_local_source.md)
already gives
\[
 I_N(-2,z)=N^{-2}A(z)e^{NP(z)}\{1+\varepsilon_N^{\rm loc}(z)\},
 \qquad \sup|\varepsilon_N^{\rm loc}|\le C/N,
 \tag{12}
\]
with a holomorphic error on a fixed neighborhood. Intersect the
finitely many neighborhoods above and shrink so that \(A\) is
bounded away from zero. Equations (8)--(12) give
\[
 \varepsilon_N(z)=\varepsilon_N^{\rm loc}(z)
 +\frac{N^2e^{-NP(z)}}{A(z)}
       \{E_N^-(-2,z)+R_N^+(-2,e^{-2\pi iz})\}.
 \tag{13}
\]
The second term is \(O(N^2e^{-\eta' N})\), where
\(\eta'=\min(\eta,\gamma/2)>0\). It is absorbed in \(O(N^{-1})\).
This proves (5). Fixed-radius Cauchy estimates prove (6).
Since \(|\varepsilon_N|<1/2\) eventually, (5) gives nonvanishing;
taking absolute logarithms gives (7).

## 3. What is still needed for composition

This theorem allows the outgoing coordinate to vary independently
near its geometric reference. It does not estimate incoming
ordinary derivatives of the whole transfer. For those derivatives,
the adjoining contribution in (8) must also be controlled on an
incoming-color neighborhood; a bound at \(w=-2\) alone is insufficient.
The local integral and \(E_N^-\) already have that larger scope.

The outgoing coordinate in (3) is an auxiliary variable, not the
ordinary right boundary color. The original closing operation is a
further finite sum over all its physical values. Formula (5) cannot
be substituted throughout that sum without bounds on its other
regions. Closing and stability under arbitrary short fillings remain
separate requirements.

## Source versions

- Original local integral, action and coefficient:
  f75fe4196fed3561381bef59bf446f00ba428101dab62d61990c91e0bdf9c696.
- Left remainder on a complex neighborhood:
  fbdc20aba05f2895e1fada626ff6ea8f26b7c8e6300a76fd6c51bb16b9c6f092.
- Physical action anchor:
  3ba93da54e86226990fe844cd245b8a973650ca84c0ca0088e9cdc579594d967.
- Endpoint dominance:
  85d5c740d1c8c3481f5d6be5dd29d826879a366f5d07a079700cb4cbd7c92804.
- Outgoing boundary extension:
  74bca3cd11850a0ab0b507de69fb42ae6e73d61434dc1bc67b1872bd5710d54a.

No mathematical numerical evaluation is used.
