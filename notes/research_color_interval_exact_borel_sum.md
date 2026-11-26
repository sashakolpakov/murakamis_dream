# An exact Borel sum for the original color interval

Private written proof, 18 November 2026.

On a specified initial color chart, the canonical Borel defect is
summable along the negative real ray and its sum is exactly the
ordinary q-Pochhammer interval. The proof evaluates the Laplace
integral directly; matching formal coefficients alone is not used
as an analytic uniqueness assertion.

All lower and upper endpoint constants are retained. This supplies
one scalar analytic source adapter. It makes no claim about the
singular lower endpoint of an unregularized factorial, finite
Poisson walls, normal products, hard contraction, or the knot cycle.

## 1. Domain and normalization

Use the product base \(q=e^h\) of [P], and initially take
\[
 \operatorname{Re}h<0,\qquad
                    |Z|<1,\qquad |Ze^s|<1.
 \tag{1}
\]
Both \(h\) and the logarithmic endpoint \(s\) are independent.
For fixed \(Z\ne0\), the endpoints zero and \(s\) lie in the
convex half-plane \(\operatorname{Re}t<-\log|Z|\). On that
half-plane define
\[
 F_Z(t)=\log(1-Ze^t)
             =-\sum_{m\ge1}\frac{Z^m e^{mt}}m.
 \tag{2}
\]
For \(Z=0\) use its holomorphic limiting value. The same series
specifies the branch at both endpoints and along the straight
segment between them. Put
\[
 J_Z(s)=\int_0^s F_Z(t)\,dt
       =\sum_{m\ge1}\frac{Z^m(1-e^{ms})}{m^2},
 \quad
 v_{0,c}=B_1(c)\bigl(F_Z(s)-F_Z(0)\bigr).
 \tag{3}
\]
Let \(\widehat V_c\) be the exact ordinary Borel germ of [D],
with convention \(\mathcal B_0(h^j)=\xi^j/j!\), and set
\(g_c=\partial_\xi\widehat V_c\). Subtracting the constant
\(F_Z(0)\) from \(F_Z\) does not alter this defect.

The negative ray is oriented from zero to negative infinity.
For \(c=0\) or \(1\), define
\[
 \mathcal S_-V_c(h;s,Z)
       =v_{0,c}+\int_0^{-\infty}e^{-\xi/h}g_c(\xi;s,Z)\,d\xi.
 \tag{4}
\]
The theorem below proves convergence, including local uniformity
in all parameters satisfying (1).

**Theorem.** For \(c=0,1\) on (1),
\[
 \boxed{\quad
 \frac{J_Z(s)}h+\mathcal S_-V_c(h;s,Z)
     =\log\frac{P(Zq^c;q)}{P(Ze^sq^c;q)}.
 \quad}
 \tag{5}
\]
The logarithm on the right is its value continued from \(Z=0\).
In this domain neither product has a zero, so this marking is
unambiguous. Exponentiating (5) gives the actual scalar interval
of [P], not a newly normalized function.

## 2. A partial fraction identity from the Bernoulli coefficients

Write \(\omega_n=2\pi i n\). The elementary Fourier proof in
[D] gives, for every \(a\ge2\),
\[
               \frac{B_a(0)}{a!}=\frac{B_a(1)}{a!}
                              =-\sum_{n\ne0}\omega_n^{-a}.
 \tag{6}
\]
Consequently, near \(t=0\),
\[
 \frac{e^{ct}}{e^t-1}-\frac1t-B_1(c)
             =-t\sum_{n\ne0}\frac1{\omega_n(\omega_n-t)},
                      \qquad c=0,1.
 \tag{7}
\]
Indeed expand each denominator on the right; the coefficient of
\(t^{a-1}\) is exactly (6). This is absolutely convergent near
zero. The right side of (7) converges normally on compact sets
avoiding the nonzero \(\omega_n\), since its tail is \(O(n^{-2})\).
It is meromorphic on the plane, as is the left side. Analytic
identity from the connected complement of their discrete pole
set proves (7) everywhere on that complement. The origin is
removable on both sides. Thus no quoted partial fraction theorem
is needed. Notice that the two choices of \(c\) have the same
left side after retaining their respective \(B_1(c)\).

## 3. The actual negative-ray defect is bounded

For \(c=0,1\), [D]'s exact meromorphic derivative is
\[
 g_c(\xi)
     =-\sum_{n\ne0}\omega_n^{-2}
       \left\{F_Z'\left(s+\frac\xi{\omega_n}\right)
                     -F_Z'\left(\frac\xi{\omega_n}\right)\right\}.
 \tag{8}
\]
On the real negative \(\xi\)-ray, each \(\xi/\omega_n\) is
purely imaginary. Hence the translated arguments have the same
\(|Ze^t|\) as their respective original endpoints. On a compact
subdomain of (1), choose \(0<r<1\) with
\(|Z|,|Ze^s|\le r\). Then all translated series stay on their
original logarithmic branches and
\[
 \left|F_Z'\left(s+\frac\xi{\omega_n}\right)
               -F_Z'\left(\frac\xi{\omega_n}\right)\right|
          \le \frac{2r}{1-r}.
 \tag{9}
\]
Thus (8) converges normally along the whole ray and is uniformly
bounded there by a constant depending only on \(r\).

Since \(\operatorname{Re}(1/h)<0\), the exponential in (4)
decays along that ray. Equations (8)--(9) prove absolute convergence
and local uniformity of (4). They also prove that the continued
ordinary Borel function has at most linear growth there:
\[
            |\widehat V_c(\xi)|\le |v_{0,c}|+C_r|\xi|.
 \tag{10}
\]
Therefore its finite endpoint companion vanishes at negative
infinity. Direct integration by parts, with the value at zero
retained, gives the equivalent ordinary Borel sum
\[
             \mathcal S_-V_c
                 =h^{-1}\int_0^{-\infty}
                           e^{-\xi/h}\widehat V_c(\xi)\,d\xi.
 \tag{11}
\]
There is no unrecorded finite-endpoint term in (11); it vanishes
because of (10) and the strict left-half-plane damping.

## 4. Direct evaluation of the Laplace transform

Expand the derivatives in (8), using (2). On the ray,
\[
 g_c(\xi)
   =-\sum_{m\ge1}\sum_{n\ne0}
      \frac{Z^m(1-e^{ms})}{\omega_n^2}
                                      e^{m\xi/\omega_n}.
 \tag{12}
\]
The sum of absolute values is bounded by
\(2\sum_{m\ge1}r^m\sum_{n\ne0}|\omega_n|^{-2}\), independently
of the ray parameter. Multiplying by the integrable damping
in (4) justifies interchanging both sums and the integral.
The elementary oriented integral is
\[
 \int_0^{-\infty}e^{-\xi/h+m\xi/\omega_n}\,d\xi
                          =\frac{h}{1-mh/\omega_n}.
 \tag{13}
\]
Its convergence follows from \(\operatorname{Re}(1/h)<0\),
since \(m/\omega_n\) is purely imaginary. Thus
\[
 \mathcal S_-V_c
   =\sum_{m\ge1}Z^m(1-e^{ms})
        \left\{\frac{B_1(c)}m
          -h\sum_{n\ne0}\frac1{\omega_n(\omega_n-mh)}\right\}.
 \tag{14}
\]
Apply (7) with \(t=mh\), divide it by \(m\), and add
\(J_Z(s)/h\) from (3). The result is
\[
 \frac{J_Z(s)}h+\mathcal S_-V_c
     =\sum_{m\ge1}
          \frac{Z^m(1-e^{ms})e^{cmh}}{m(e^{mh}-1)}.
 \tag{15}
\]
The convergent product proof in [P] identifies this last expression
with the logarithm on the right of (5). Alternatively expand each
product logarithm into \(-\sum A^m/m\) and sum its convergent
geometric \(q\)-tail; this gives (15) directly. For \(c=0,1\),
the inequalities (1) and \(|q|<1\) justify this expansion.
Every operation is absolutely convergent. This proves (5) as
an analytic identity, not merely an equality of formal expansions.

## 5. Fixed integer offsets and quantum pointing

For a fixed integer \(c\), [D] gives the exact finite oriented
endpoint correction
\[
 \widehat V_c-\widehat V_0
   =\sum_{d\in[0,c)}^{\mathrm{or}}
                \{\mathcal E_d(\xi;s)-\mathcal E_d(\xi;0)\},
 \quad
 \mathcal E_d(\xi;t)
      =\sum_{j\ge0}\frac{d^jF_Z^{(j)}(t)}{(j!)^2}\xi^j.
 \tag{16}
\]
Choose common endpoint Cauchy disks of radius \(\delta>0\),
with \(|F_Z|\le M\). Then
\( |\mathcal E_d(\xi;t)|\le M e^{|d\xi|/\delta}\).
Let \(D_c\) be the maximum of \(|d|\) in this finite sum,
with value zero for an empty sum. Under the additional condition
\[
                       -\operatorname{Re}(1/h)>D_c/\delta,
 \tag{17}
\]
the ordinary Laplace transform of every term in (16) converges
absolutely. Termwise integration is justified by the same bound;
\[
 h^{-1}\int_0^{-\infty}e^{-\xi/h}\xi^j\,d\xi=j!h^j
\]
then gives exactly
\[
 h^{-1}\int_0^{-\infty}e^{-\xi/h}
                       \mathcal E_d(\xi;t)\,d\xi=F_Z(t+dh).
 \tag{18}
\]
Condition (17) also implies \(|dh|<\delta\), so the Taylor sum
on the right is the stated endpoint germ. This applies uniformly
on compact endpoint charts and every sufficiently small closed
left-half-plane subsector.

The finite product identity in [P] is
\[
 \log\Pi_c-\log\Pi_0
   =\sum_{d\in[0,c)}^{\mathrm{or}}
                     \{F_Z(s+dh)-F_Z(dh)\}.
 \tag{19}
\]
All logarithms are continued from \(Z=0\). Equations (16)--(19)
therefore extend (5) to every fixed integer offset on this smaller
domain. Negative offsets keep their oriented lower-endpoint terms;
no negative factorial is evaluated.

At \(s=hL\), \(L\ge0\), whenever the stated convergence domain
holds, exponentiating (5) gives exactly
\[
 \exp\{J_Z(hL)/h+\mathcal S_-V_c(h;hL,Z)\}
                              =(Zq^c;q)_L.
 \tag{20}
\]
For \(c=0,1\), every \(|Z|<1\), \(\operatorname{Re}h<0\),
and nonnegative \(L\) obeys (1). For other offsets retain (17).
After this lattice restriction, the whole finite product on the
right has its unique meromorphic continuation in the parameters
and its polynomial root values as in [P]. This does not assert
that the same straight Borel ray remains admissible after those
parameters leave the domain of this proof.

The normalized endpoint function \(F_Z(t)-F_Z(0)\) has the same
defect. Its principal term must still be supplemented by
\((s/h)\log(1-Z)\); on the lattice this is the original whole
peripheral factor \((1-Z)^L\). Thus the analytic comparison
retains that factor rather than specializing it away.

## 6. What this exact comparison does not settle

The proof selects the canonical negative-ray branch on (1) and
evaluates its integral. It therefore removes the periodic ambiguity
for this particular scalar sum. Other continued branches still
have their explicitly retained monodromy; integer pointing alone
does not remove all off-lattice periodic factors.

The factorial specialization \(Z=1\) lies outside (1), and its
unnormalized lower endpoint is singular. Its separate classical
factor and the regularized \(F_0\) interval need their own analytic
comparison. Nor does (20) identify a finite Poisson projection's
upper-wall terms with a Borel cutoff endpoint, or justify an
untruncated signed trace. The source's normal products and hard
Gaussian assembly, full original-prefix action-difference domains,
and the original relative cycle remain separate steps.
The initial disks \(|Z|<1\) for positive and negative color
intervals need not give one common meridian chart for a mixed
word. This scalar identity does not assert such a common chart;
its source use outside these disks requires the corresponding
continued scalar branches and their contours.

## 7. Complete proof directs

| Label | Complete proof source | SHA256 |
|---|---|---|
| D | notes/research_literal_interval_global_borel_log.md | d0885ed0ae7f050ad72d8d128a1edb7bef4200f1b02f624612a8946bbef72a2e |
| P | notes/research_q_pochhammer_interval_lattice_anchor.md | 6ea92b17088e3dcac62fedc3b64a922be41c04be2637e94adfc306dd123f8275 |

D supplies the exact Borel function, its elementary Bernoulli proof,
and integer-offset entire corrections. P supplies the original
interval, its convergent product, and its exact lattice/source
normalization. Both complete texts were read and all used
implications checked. The negative-ray estimates and exact Laplace
evaluation are proved above. No imported summation theorem or
mathematical program, test, or build is used. Frozen manuscripts
and public files are unchanged.
