# A weighted norm for the half-period transfer operators

Research deduction, 5 November 2026. The boundary potential constructed
in [the open-chain argument](research_mixed_nonlow_open_chain_boundary.md)
gives a concrete answer to one part of the proposed Cauchy–Schwarz approach:
there is a weighted Hilbert norm in which successive blocks have no
positive exponential growth after their geometric normalization. This
is an upper estimate. It does not prove an almost-invariant vector or
the nonvanishing of a particular matrix coefficient.

## 1. The state and the boundary term in the tangent

Fix the periodic type word, its original critical reference, and the
notation of that argument. A state at layer \(j\) is the triple
\(v=(q_{j-2},q_{j-1},q_j)\), where a symbol records a real coordinate
in \([.1,.5]\) and an allowed selection. Appending \(q_{j+1}\)
gives the state \(v'=(q_{j-1},q_j,q_{j+1})\). The middle target
\(z_{j-1}\) is determined by \(v\); the next target \(z_j\) is
determined by \(v'\). This is why the three-symbol state is needed.

Write
\[
 P_j=\partial_b\phi_j(r_{j-1},r_j),\qquad
 c_j=\Re\phi_j(r_{j-1},r_j),\qquad
 T_j(v)=\Re\{P_{j-1}(z_{j-1}(v)-r_{j-1})\}.
 \tag{1}
\]
Here \(c_j\) is a real edge action, not a contour height. Original
criticality says
\(\partial_a\phi_j(r_{j-1},r_j)=-P_{j-1}\). Consequently the
full geometric tangent satisfies the exact identity
\[
 \Re\Gamma_j(z_{j-1},z_j)
       =c_j+T_{j+1}(v')-T_j(v).
 \tag{2}
\]
This identity also holds for primitive periods one and two, with both
partial derivatives and the original incidences retained.

Let \(\mathcal H_j\) be the continuous potential of the open-chain
theorem, with its incoming-path convention:
\[
 w_j(v,v')\le\mathcal H_{j+1}(v')-\mathcal H_j(v).
 \tag{3}
\]
Define
\(\mathcal V_j=T_j+\mathcal H_j\). If \(e_j(v,v')\) is the
complete upper phase of one allocated block, including half of each
endpoint's selected Fourier correction, then \(e_j=\Re\Gamma_j+w_j\).
Equations (2)–(3) give
\[
 e_j(v,v')\le c_j+\mathcal V_{j+1}(v')-\mathcal V_j(v).
 \tag{4}
\]
Every \(\mathcal V_j\) vanishes at its reference state. The potentials
are uniformly bounded over the compact local domains, including when
the fixed word length varies. Their construction still uses the actual
critical reference of the word.

## 2. A Hilbert-space estimate with no lost exponential factor

Choose a probability measure \(\mu_j\) on the symbol space at each
layer. Examples are normalized Lebesgue measure on the real interval,
with normalized counting measure on selections, or normalized counting
measure on a finite mesh. The product measure on states is
\(\nu_j=\mu_{j-2}\otimes\mu_{j-1}\otimes\mu_j\).
The following argument works for either choice.

Let \(\mathcal B_{j,N}(v,v')\) be the allocated nonnegative block
modulus from the open-chain theorem. In particular it uses the modulus
of the complete conditional finite sum, not the sum of the moduli of
its rows. The Fourier halfweights are nonnegative real square roots
of moduli; no complex square-root branch is being introduced. Their
product restores the original integer weights at internal vertices.

The proved finite-source estimate and (4) imply, for every
\(\eta>0\),
\[
 \mathcal B_{j,N}(v,v')
 \le C_{j,\eta}N^{a_j}
  \exp N\{c_j+\mathcal V_{j+1}(v')-\mathcal V_j(v)+\eta\}
 \tag{5}
\]
uniformly on the full compact symbol domain, at all sufficiently large
integer levels and both parities. All allowed selections remain in
this estimate.

For any measurable complex kernel \(K_{j,N}\) satisfying
\(|K_{j,N}|\le\mathcal B_{j,N}\), define the transfer operator by
\[
 (\mathsf T_{j,N}f)(q_{j-1},q_j,q_{j+1})
 =\int K_{j,N}(q_{j-2},q_{j-1},q_j,q_{j+1})
             f(q_{j-2},q_{j-1},q_j)\,d\mu_{j-2}.
 \tag{6}
\]
The positive kernel \(K_{j,N}=\mathcal B_{j,N}\) is itself allowed.
Using normalized selection measures changes an unnormalized finite
selection sum by only its fixed counting factors, which must be restored
when applying the estimate to that sum.

Equip the state space with the weighted norm
\[
 \|f\|_{j,N}^2=
     \int |f(v)|^2e^{-2N\mathcal V_j(v)}\,d\nu_j(v).
 \tag{7}
\]
Multiplication by \(e^{-N\mathcal V_j}\) is an isometry from
this weighted space onto \(L^2(\nu_j)\). After these isometries and
the scalar normalization \(e^{-Nc_j}\), the kernel in (6) has
modulus at most \(C_{j,\eta}N^{a_j}e^{N\eta}\), by (5).

**Theorem 1.** The operator between the weighted spaces satisfies
\[
 \|\mathsf T_{j,N}\|_{j,N\to j+1,N}
       \le C_{j,\eta}N^{a_j}e^{N(c_j+\eta)}.
 \tag{8}
\]

**Proof.** It suffices to estimate an unweighted transfer operator whose
kernel has modulus at most a constant \(D\). For fixed
\((q_{j-1},q_j,q_{j+1})\), Cauchy–Schwarz in the probability measure
\(\mu_{j-2}\) gives
\[
 |\mathsf T f|^2
 \le D^2\int |f(q_{j-2},q_{j-1},q_j)|^2\,d\mu_{j-2}.
 \tag{9}
\]
Integrating in the three output variables leaves exactly
\(D^2\|f\|_{L^2(\nu_j)}^2\): the new variable has total measure
one. Apply this to the conjugated kernel with
\(D=C_{j,\eta}N^{a_j}e^{N\eta}\), and restore
\(e^{Nc_j}\). This proves (8). No positivity of \(K_{j,N}\)
is used. \(\square\)

For every fixed number \(n\) of consecutive blocks, choose
\(\eta<\delta/n\) in each factor. Submultiplicativity then gives
\[
 \|\mathsf T_{a+n-1,N}\cdots\mathsf T_{a,N}\|
 \le C_{n,\delta}N^{A_n}
       \exp N\left\{\sum_{j=a}^{a+n-1}c_j+\delta\right\}.
 \tag{10}
\]
The norm on the left is between the corresponding weighted endpoint
spaces. For fixed \(n\), its upper exponential rate is at most the
sum of the edge actions. No uniform statement when \(n\) grows with
\(N\) follows from (10).

## 3. Keeping the loss away from the reference

The [additive occupation theorem](research_mixed_nonlow_occupation_loss.md)
strengthens (3). Define the plateau clamp and the nonnegative penalty
\[
 y_j=\max\{.22,\min\{x_j,.45\}\},\qquad
 \omega_j(q_j)=\frac{\min\{1,\sigma_j+400(y_j-\Re r_j)^2\}}{3200000}
                         +\frac{(x_j-.45)_+}{10}.
 \tag{11}
\]
Here \(t_+=\max\{t,0\}\). That theorem supplies a continuous
reference-normalized potential \(\widehat{\mathcal H}\) with
\[
 w_j(v,v')+\omega_j(q_j)
       \le\widehat{\mathcal H}_{j+1}(v')-
                         \widehat{\mathcal H}_j(v).
 \tag{12}
\]
Use \(\widehat{\mathcal V}=T+\widehat{\mathcal H}\) in the
weighted norm, denoted by \(\|\cdot\|_{\widehat{\mathcal V},j,N}\).
Since \(q_j\)
is part of the input state in (6), exactly the same proof gives
\[
 \|\mathsf T_{j,N}f\|_{\widehat{\mathcal V},j+1,N}
 \le C_{j,\eta}N^{a_j}e^{N(c_j+\eta)}
                 \|e^{-N\omega_j(q_j)}f\|_{\widehat{\mathcal V},j,N}.
 \tag{13}
\]
Indeed, the conjugated kernel acquires the additional upper factor
\(e^{-N\omega_j(q_j)}\), which is constant in the forgotten
integration variable. It can be included in the input before applying
Cauchy–Schwarz.

For example, if \(f\) is supported where the last symbol is selected
or its real coordinate lies outside \([.22,.45]\), then
\(\omega_j\ge1/3200000\) on that support. Equation (13) retains
that strict exponential loss after the normalization \(e^{-Nc_j}\),
with any source tolerance smaller than it. This is a bound on
specified input support, not a spectral gap assertion for the whole
operator or a construction of an almost-invariant vector.

## 4. What this contributes to a gluing argument

The norm is obtained from a proved boundary potential, rather than
postulated as a favorable inner product. It prevents repeated interior
steps from accumulating an additional positive exponential rate.
However, the weights in (7) depend exponentially on \(N\). Converting
an arbitrary physical boundary vector to this norm can therefore have
an exponential cost. Its actual boundary values must be estimated;
boundedness of \(\mathcal V\) alone does not remove that cost.

Nor does an upper operator bound imply a lower bound for a specified
contraction. Even on a two-dimensional Hilbert space, a unitary swap
has norm one and sends a unit vector to an orthogonal unit vector.
Its matrix coefficient against the original vector is zero. In the
present problem one still needs a nonzero overlap with the geometric
contribution and control of the other contributions. Neither is a
consequence of (8).

Finally, (6) is a transfer estimate for the stated block kernels. It
does not identify an arbitrary state-space operator with Kashaev's
entire invariant. The original contour Jacobian, exact boundary
functionals, scalar normalization and restored selection counts must
be retained in any such application. The contour Jacobian has the
already proved bound independent of \(N\) at each fixed word length.
Coordinates outside \([.1,.5]\), arbitrary short fillings, and a
universal family of almost-invariant vectors remain outside this
deduction.
