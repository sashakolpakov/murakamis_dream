# Terminal branches stabilize a complete local source

Private structural deduction, 10 November 2026. An exact polynomial
source with a full nonzero local packet need not satisfy the global
boundary estimate required for subsequent long fillings. This note
proves that finitely many actual terminal branches at each free
boundary supply that estimate. It therefore gives a closure
implication for decorated sources, not for the undecorated source.
In particular it neither completes the symmetric \(343\) assembly
nor proves a finite-exception or knot theorem.

No mathematical numerical evaluation is used.

## 1. Inputs and the exact decoration

Let \(r\geq1\) be fixed. Suppose the entire original source is
\[
 Q_N(\mathbf t)=q_N(-2\cos t_1,\ldots,-2\cos t_r),
 \qquad \deg_{w_j}q_N\leq d_jN ,
 \tag{1}
\]
where \(d_j\) are fixed constants. On a neighborhood of one fixed
closed angular polydisk about zero suppose
\[
 Q_N(\mathbf t)=\epsilon_NN^\alpha a(\mathbf t)e^{NW(\mathbf t)}
                    (1+E_N(\mathbf t)),\qquad
 |\epsilon_N|=1,\quad E_N=O_{\rm hol}(N^{-1}),\quad a(0)\ne0 .
 \tag{2}
\]
The phase \(W\) is separately even and independent of \(N\).
All factors in (2) refer to the full finite polynomial, rather
than one retained sector. A negative real Hessian for \(W\) is
not assumed.

Use the original terminal power two,
\[
 H_N(t)=T(R^2)(-2\cos t)
       =\phi_N^{(x)}[R(x)^2K_N(x,-2\cos t)] .
 \tag{3}
\]
Sections 2, 4 and 5 of the
[terminal-source theorem](research_verified_terminal_fillings_and_long_remainder.md)
give its literal full-source properties
\[
\begin{split}
 H_N(t)&=\varepsilon_{2,N}a_2(t)e^{Nh(t)}
                         (1+O_{\rm hol}(N^{-1})),\\
 \varepsilon_{2,N}&=e^{i\pi N/2},\qquad a_2(0)\ne0,\qquad
 a_H:=-\Re h''(0)>0,\\
 |H_N(x+iy)|&\leq C_HN^{A_H}
       e^{N\{M_H-c_H(1-\cos x)+B_Hy^2\}},
       \qquad M_H=\Re h(0),\quad c_H>0 .
\end{split}                                                        \tag{4}
\]
The last line holds on a fixed strip about the whole real period.
The phase \(h\) is the calibrated geometric terminal phase in
that source; its explicit imaginary constant is in
\(\varepsilon_{2,N}\). Its ordinary degree is at most \(N-1\).

For a fixed nonnegative integer \(m\), form the exact unreduced
polynomial
\[
 \widetilde Q_{m,N}(\mathbf t)
       =Q_N(\mathbf t)\prod_{j=1}^r H_N(t_j)^m .
 \tag{5}
\]
Each factor in (3) is a different original terminal vertex and
its edge. Thus (5) represents \(m\) actual terminal branches at
each boundary vertex, whenever those boundary slots are realized
by an original ordered tree. It is not a change of the source at
the same fixed template. Its separate degrees are at most
\(d_jN+m(N-1)\); multiplication precedes quotient reduction.

## 2. A finite global ceiling follows from the local packet and degree

There are constants \(B,C,A\), independent of \(N\), such that
\[
 \sup_{\mathbf w\in[-2,2]^r}|q_N(\mathbf w)|
                         \leq CN^A e^{NB}.                         \tag{6}
\]
This is deliberately only a coarse ceiling. It is not asserted
that \(B\leq\Re W(0)\).

Here is a direct proof, so (6) requires no new norm estimate for
the source. Choose \(0<\rho<\pi\) inside the real box of (2), and
put
\[
 I=[-2,-2\cos\rho],\quad \ell=2(1-\cos\rho),\quad
 L=8/\ell-1>1,\quad \mathcal R=L+\sqrt{L^2-1}.
 \tag{7}
\]
The affine coordinate \(\tau(w)=2(w+2)/\ell-1\) maps \(I\) to
\([-1,1]\), and maps \([-2,2]\) into \([-1,L]\).
The packet gives
\[
 \|q_N\|_{I^r}\leq C_0N^{A_0}e^{NM_{\rm loc}},\qquad
 M_{\rm loc}=\max_{\mathbf x\in[0,\rho]^r}\Re W(\mathbf x).
 \tag{8}
\]
Expand \(q_N\) in the tensor Chebyshev basis \(T_{k_j}(\tau(w_j))\).
The usual cosine coefficient integrals bound each coefficient
by \(2^r\|q_N\|_{I^r}\). For \(-1\leq v\leq L\),
\(\lvert T_k(v)\rvert\leq\mathcal R^k\). There are at most
\(\prod_j(\lfloor d_jN\rfloor+1)\) coefficients. Consequently
(6) holds with
\[
                  B=M_{\rm loc}+\sum_jd_j\log\mathcal R .
 \tag{9}
\]
This argument applies to complex polynomial coefficients. It
uses a genuine interval in every ordinary variable, not a
single complete-color value or finitely many jets.

## 3. The calibrated real gap and full strip bound

**Theorem 1.** For every source (1)--(2), there is a fixed integer
\(m_0\) such that, for every fixed \(m\geq m_0\), the entire
polynomial (5) has a nonzero holomorphic packet
\[
\begin{split}
 \widetilde Q_{m,N}
  &=\epsilon_N\varepsilon_{2,N}^{mr}N^\alpha
      \widetilde a_m e^{N\widetilde W_m}
                          (1+O_{\rm hol}(N^{-1})),\\
 \widetilde a_m(\mathbf t)&=a(\mathbf t)\prod_j a_2(t_j)^m,
 \qquad
 \widetilde W_m(\mathbf t)=W(\mathbf t)+m\sum_jh(t_j),
\end{split}                                                        \tag{10}
\]
and constants \(c_m,B_m,b_m>0,C_m,A_m\) such that
\[
 |\widetilde Q_{m,N}(\mathbf x+i\mathbf y)|
 \leq C_mN^{A_m}
   e^{N\{M_m-c_m\sum_j(1-\cos x_j)+B_m\|\mathbf y\|_2^2\}},
 \quad |x_j|\leq\pi,\quad |y_j|\leq b_m ,
 \tag{11}
\]
where \(M_m=\Re W(0)+mrM_H\). Its complete-boundary Hessian
has strictly negative real part. All constants and \(m\) are
chosen before \(N\).

*Proof.* First choose one smaller angular polydisk on which
\(a,a_2\) are zero-free and
\(-\Re h''\geq a_H/2\). Let \(L_W\) bound the operator norm of
the Hermitian real part of \(W''\) there. Choose \(m\) so
\[
                     ma_H/2-L_W\geq1 .
 \tag{12}
\]
Then \(-\Re\widetilde W_m''\succeq I\) throughout that
polydisk. In particular, on a fixed real box
\(\|\mathbf x\|_\infty\leq\rho\) contained in it, separate
evenness and integration twice imply
\[
 \Re\widetilde W_m(\mathbf x)
       \leq M_m-\tfrac12\|\mathbf x\|_2^2
       \leq M_m-\sum_j(1-\cos x_j).
 \tag{13}
\]
The finite product of the full local expansions proves (10),
including its holomorphic error. The number of factors is fixed.

For the complement of that box, (4) and (6) give
\[
 |\widetilde Q_{m,N}(\mathbf x)|
 \leq CN^A e^{N\{M_m+B-\Re W(0)
                         -mc_H\sum_j(1-\cos x_j)\}} .
 \tag{14}
\]
There \(\sum_j(1-\cos x_j)\geq s_\rho:=1-\cos\rho>0\).
Increase the fixed \(m\), if needed, so that
\[
        \frac{mc_Hs_\rho}{2}>
                       \max\{B-\Re W(0),0\}.                     \tag{15}
\]
The right side of (14) then has rate at most
\(M_m-(mc_H/2)\sum_j(1-\cos x_j)\).
Together with (10),(13), this proves a calibrated global real
angular bound, with coefficient
\(\min\{1,mc_H/2\}>0\).

Apply Lemma 1 of the
[local-packet/real-gap reduction](research_mixed_open_source_stability_reduction.md)
to this full polynomial. Its degree is a fixed multiple of \(N\)
in every variable, its local Hessian is negative by (12), and
the just-proved real bound has a fixed gap outside a fixed box.
That lemma proves precisely the quadratic strip estimate (11).
It uses the finite degree and the full real bound; it does not
continue an asymptotic from a single point. \(\square\)

## 4. Complete subsequent long fillings

For every fixed \(m\geq m_0\), Theorem 1 satisfies all hypotheses
of the
[complex-phase long-filling theorem](research_long_fillings_complex_boundary_phase.md).
Consequently there is a threshold \(n_0(m,Q)\) such that all
independently chosen fixed signed powers \(|n_j|\geq n_0(m,Q)\)
give the complete asymptotic
\[
\begin{split}
 \left(\bigotimes_{j=1}^r\phi_N^{(j)}R_j^{n_j}\right)
       \widetilde Q_{m,N}
 ={}&\epsilon_N\varepsilon_{2,N}^{mr}
     \left(\prod_jC_{N,n_j}\right)
     N^{\alpha+3r/2}D_{m,\mathbf n}
     e^{N\mathcal S_{m,\mathbf n}}
                          (1+O(N^{-1})),\\
                         &D_{m,\mathbf n}\ne0 .
\end{split}                                                        \tag{16}
\]
The stationary action is the original-charge stationary value
of
\[
 \widetilde W_m(\mathbf t)
       +\frac{i}{4\pi}\sum_j n_jt_j^2-i\sum_jt_j .
 \tag{17}
\]
Here \(C_{N,n}=q^{n(N-1)^2/4}\) with the original
\(q=e^{\pi i/N}\). The coefficient in (16) is exactly formula
(5) of that theorem with amplitude \(\widetilde a_m\).
It includes the original sine factors and Gaussian branch.
The theorem's complete rational trace retains every Fourier
charge, endpoint current, double-root normal and odd simple
node. No value-only trace or principal-charge replacement is
being used in (16).

For a two-boundary tree source with \(\alpha=-3/2\), the final
power is \(N^{3/2}\). Adding one terminal branch adds one
selected vertex and one edge, and the already summed terminal
has level power zero. This explains why the decoration does not
alter that count.

There is also an iterated version. Let a fixed finite collection
\(E_{j,N}(s,u)\) satisfy (1)--(2) with two variables and power
\(N^{-3/2}\). Decorate every member as in (5), choosing one common
\(m\) by finiteness. Then the exact operations
\[
 F_N\longmapsto
 \phi_N^{(s)}[R(s)^nF_N(s)\widetilde E_{j,m,N}(s,u)]
 \tag{18}
\]
preserve a common controlled one-boundary class for all fixed
sufficiently long signed \(n\). One threshold works for every
fixed finite sequence, independently of its length and of the
order of this finite collection, starting for example with the
original \(F_N=H_N\) in (3). A sufficiently long final original
trace has a nonzero complete asymptotic.

For clarity, the degree-\((N-1)\) wording in the
[finite-kernel induction](research_finite_two_boundary_kernel_closure.md)
requires one explicit adjustment here. Its proof uses that
degree bound only for polynomial-cost Markov estimates and
for linear-cost strip continuation. Replace it throughout by
the common fixed bound \(dN\), where \(d\) dominates the degrees
of all decorated kernels. Markov costs become \(O(d^2N^2)\);
the maximum-principle strip cost becomes \(d|\Im u|\) in rate.
Choose the common strip and thresholds after this fixed \(d\).
The exact complete trace is valid for arbitrary polynomial
degree, as explicitly retained in the complex-phase theorem
and the [unreduced gluing bound](research_calibrated_remainders_under_finite_gluing.md).
Integration in \(s\) leaves the output degree bounded by the
degree of \(\widetilde E_{j,m,N}\) in \(u\); degrees do not grow
with the number of operations. All other steps of that induction
use its local packet, negative Hessian and whole strip bound,
which Theorem 1 supplies. Its phase reset, Schur-complement sign,
output angular-loss reset and nonzero coefficient therefore
apply unchanged. Polynomial prefactors and starting levels may
depend on the entire fixed sequence.

## 5. What this proves, and what it does not

This is a closure theorem for an actual modification of a source.
If the complete ordinary \(343\) polynomial acquires its full
bidisk packet, it can be used as one of the \(E_j\) above without
first proving an undecorated whole two-boundary angular gap.
That application is conditional here on the completed whole
packet, not on its already proved local contour contribution.
For several prescribed short pieces one chooses a finite
decoration and one common long-separator threshold.

The conclusion is an exact finite-boundary asymptotic. A
geometric or knot interpretation additionally requires the
original marked boundary germs and their compatible face maps,
primitive periods, positive fillings and absolute action
anchors. The terminal factors have those data by their cited
source. They do not supply missing markings for an arbitrary
input polynomial. Actual strand tracing, the reduced cut and
the prescribed zero-framing normalization must also be checked.
No such topological conclusion is asserted by (16) alone.

The new branches change the original template and its boundary
degrees. Their effect cannot be removed after the estimate.
In particular this theorem does not establish short-filling
stability for the original undecorated template. The explicit
local-packet/turn obstruction in the
[Fourier observation scope note](research_mixed_next_fourier_observation_composition_scope.md)
still applies when the global input is absent.

For the finite-exception objective, an applicable source or
exact reduction theorem is still needed at every visited
partial assignment, including incompatible signs, branching
short components and hyperbolic descendants of nonhyperbolic
intermediate fillings. Thresholds need not be uniform over
those nodes. Moreover the
[original-tree padding equivalence](research_original_tree_padding_equivalence.md)
shows why an untreated reduced core cannot be counted as one
exception: its original assignment fiber can already be infinite.
The present decoration theorem does not resolve that obligation.

## Source bindings

- Terminal full-source properties, exact phase and scalar:
  research_verified_terminal_fillings_and_long_remainder.md,
  SHA-256 f41b02ba17d8db4791434f26ec06ab4665cb0064a615ddd56361da3b4740dc1f.
- Local packet plus calibrated real gap:
  research_mixed_open_source_stability_reduction.md,
  SHA-256 5d501024dddb98ff28f1ae3d44110d4a34bfc82d8063ff01353315c3efbfc31c.
- Complete multivariate long traces:
  research_long_fillings_complex_boundary_phase.md,
  SHA-256 bffa5dfe8da7268c65d5e96bf1b1cdfa0328b084af01b713ac00571b26835618.
- Finite collection and unchanged-disk induction:
  research_finite_two_boundary_kernel_closure.md,
  SHA-256 759118c877a9657355d5c457bfc3d0b7a45cc2601a8b247f4e030c90770155cc.
- Unreduced-degree complete gluing:
  research_calibrated_remainders_under_finite_gluing.md,
  SHA-256 7e047cb7250932bba85e51d20b3327f08b00bf6d5b7e947e4d2f3243ef39d2e0.
- Local observation obstruction:
  research_mixed_next_fourier_observation_composition_scope.md,
  SHA-256 94fcd1d0f62fd7a9040ba328c95e25aa341348e236b7246a6dca0e6e7a4dfcb2.
- Original-template padding and infinite fibers:
  research_original_tree_padding_equivalence.md,
  SHA-256 e7ee7e5d3478e663e2018f6040b7f97e852a4624c94984f01708c3862d51967f.
