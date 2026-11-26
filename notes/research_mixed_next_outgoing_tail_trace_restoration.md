# Restoring the full outgoing edge after the original inner trace

Private finite-source deduction, 9 November 2026. Contracting the
removed outgoing Newton rows in the original inner trace gives
a uniform upper bound with rate \(2b_2+|\Im u|\). On the selected
charged curve this is strictly below the inner action. This is
a fresh estimate for the difference of two ordinary polynomials;
it does not follow from their equality after an outer radical
multiplication.

No mathematical numerical evaluation, saved-value arithmetic,
or frozen-source edit is used.

## 1. Sources and exact statement

Keep the original physical algebra, trace and crossing, with
\[
 D=N-1,\quad m=\lfloor N/2\rfloor,\quad U=m-1,\quad
 c_a=2\cos((2a+1)\pi/N),\quad q=e^{\pi i/N},
\]
\[
 R_N(c_a)=\kappa(-1)^a q^{a(a+1)},\qquad
 |\kappa|=1,\qquad C_{N,3}=e^{3\pi iD^2/(4N)}.
\tag{1}
\]
Let \(K_N(x,y)=\sum_{j=0}^{D}e_j(x)e_j(y)\) be the full
ordinary kernel, and \(K_N^<(x,y)=\sum_{j=0}^{U}e_j(x)e_j(y)\).
For \(z_u=-2\cos u\), define
\[
\begin{aligned}
 Q_N^{\rm full}(u)
  &=\phi_N^{(x)}[R_N(x)^3K_N(-2,x)K_N(x,z_u)],\\
 Q_N^{\rm sh}(u)
  &=\phi_N^{(x)}[R_N(x)^3K_N(-2,x)K_N^<(x,z_u)],\\
 \Delta_N(u)&=Q_N^{\rm full}(u)-Q_N^{\rm sh}(u).
\end{aligned}
\tag{2}
\]
Both inner traces are full. All physical values, first normals
and the odd simple node retain their original meanings.

**Theorem 1.** There are fixed \(C,A\) such that, at both
parities,
\[
 |\Delta_N(u)|\le C N^A
       e^{N(2b_2+|\Im u|)},\qquad
 |\Re u|\le\pi,\quad |\Im u|\le1/2.
\tag{3}
\]
The bound also controls the sum of the absolute terms in the
exact contractions below. Here \(b_2\) is the original
real Newton constant, with \(b_2<7/12\).

On the selected curve of
[the curve packet](research_mixed_next_selected_curve_inner_packet.md),
\[
            |\Delta_N(u_\delta)|
                \le C e^{N(s(u_\delta)-1/20)}
                \qquad(0\le\delta\le1/2)
\tag{4}
\]
for all sufficiently large \(N\). Consequently the full
ordinary source has there the same nonzero relative packet
as the shortened-output source:
\[
 Q_N^{\rm full}(u_\delta)
   =C_{N,3}N^{-3/2}\mathcal A(u_\delta)e^{NS(u_\delta)}
                                     \{1+O(N^{-1})\}.
\tag{5}
\]
These are new bounds for the complete traced source; they do
not assert pointwise equality of the two kernels before trace.

## 2. Exact radical contraction of the outgoing rows

Use
[the radical contraction, Theorems 1 and 6](research_high_newton_radical_contraction.md).
For \(0\le r<m\),
\[
 \phi_N(R_N^3 e_{D-r}f)
   =\sum_{a=0}^{r}b_{ra}R_N(c_a)^3f(c_a),\qquad
 b_{ra}=(-1)^{r+a}
 \frac{s_{2a+1}S_r^2}{S_{r-a}S_{r+a+1}},\qquad |b_{ra}|\le2.
\tag{6}
\]
Here \(s_j=2\sin(\pi j/N)\) and \(S_j=\prod_{\nu=1}^j s_\nu\).
The original first normal is consumed in (6). There is no
evaluation replacement for an arbitrary trace.

At even \(N=2m\), every removed outgoing index is \(D-r\),
\(0\le r<m\), so the exact difference is
\[
 \Delta_N(u)=
  \sum_{r=0}^{m-1}e_{D-r}(z_u)
     \sum_{a=0}^{r}b_{ra}R_N(c_a)^3K_N(-2,c_a).
\tag{7}
\]
At odd \(N=2m+1\), the same expression accounts for the
removed indices \(m+1,\ldots,D\). The middle index \(m\)
must be retained separately. The exact original identity in
[first-edge tail contraction, (11)](research_mixed_next_inner_three_first_edge_tail_contraction.md)
is
\[
 \phi_N(e_m f)=
  \sum_{a=0}^{m-1}(-1)^{m+a}
            2\cos((m-a)\pi/N) f(c_a)+f(-2).
\tag{8}
\]
Thus at odd levels the right side of (7) has the additional term
\[
 e_m(z_u)\left[
  \sum_{a=0}^{m-1}(-1)^{m+a}
     2\cos((m-a)\pi/N)R_N(c_a)^3K_N(-2,c_a)
                         +C_{N,3}K_N(-2,-2)\right].
\tag{9}
\]
The last scalar is exact:
\(R_N(-2)^3=C_{N,3}\), as in the cited source.
The middle row is not treated as radical. Its simple-node
value is essential in (9).

Every coefficient and crossing value in (7),(9) is original.
In particular the fixed free endpoint in the remaining kernel
is still \(-2\); it has not been replaced by a geometric saddle.

## 3. Uniform bounds for the exact surviving terms

The radical Fourier bound gives
\[
 \|e_{D-r}(-2\cos(\,\cdot\,))\|_{\mathrm{Fourier},1}
                          \le\sqrt{N-1},
 \qquad0\le r<m.
\]
Its frequencies have modulus at most \(D\), so, for every
complex \(u\),
\[
                    |e_{D-r}(z_u)|
                    \le\sqrt{N-1}\,e^{D|\Im u|}.
\tag{10}
\]
This is a bound for the actual polynomial before contraction,
including its physical zeros and normal normalization.

For the odd middle row, the zero-safe finite-product proof in
[the far-negative source, (11)--(13)](research_mixed_next_inner_three_far_negative_source.md)
gives uniformly on the present bounded-height strip
\[
                  |e_m(z_u)|\le C N^A e^{N|\Im u|/2}.
\tag{11}
\]
Its proof retains the exact odd index
\(m/N=1/2-1/(2N)\). The full-circle logarithmic integral
has value \(|\Im u|\), its half-period profile is
\(|\Im u|/2\), and the actual endpoint displacement
costs only \(O(\log N)\). No limiting half-index value
has been substituted for the finite polynomial.

Finally the adopted all-index real Newton estimate, recorded in
[first-edge tail contraction, (17)](research_mixed_next_inner_three_first_edge_tail_contraction.md),
is
\[
             \sup_{x\in[-2,2]}|e_j(x)|
                    \le C N^A e^{Nb_2},
                       \qquad0\le j\le D.
\tag{12}
\]
Apply (12) to both factors in the literal finite kernel:
\[
           \sup_{x,y\in[-2,2]}|K_N(x,y)|
                         \le C N^A e^{2Nb_2}.
\tag{13}
\]
This is an absolute termwise estimate. It includes the
complete kernel at the odd simple point \((-2,-2)\).
At a double point \(c_a\), the terms \(j>a\) vanish,
but that extra fact is not needed to prove (13).

In (7), there are only polynomially many terms,
\(|b_{ra}|\le2\), and \(|R_N(c_a)^3|=1\).
Equations (10),(13) give their absolute sum at rate
\(2b_2+|\Im u|\).
At odd levels the coefficients in (9) have modulus at most
two, and its simple-node coefficient has modulus one.
Equations (11),(13) give rate at most the same value.
This proves (3), including its absolute-sum assertion.

## 4. Restoring the full source on the selected curve

The [selected upper depth](research_mixed_next_selected_charged_depth_bound.md)
and [action floor](research_mixed_next_selected_action_floor_and_endpoint_payment.md)
give \(K<2/5\) and \(s(u)>331/200\).
Since \(b_2<7/12\), (3) has rate strictly less than
\[
              \frac76+\frac25=\frac{47}{30},
 \qquad
              \frac{331}{200}-\frac{47}{30}=\frac{53}{600}.
\tag{14}
\]
The reserve after a claimed gap \(1/20\) is \(23/600>0\).
It absorbs every polynomial factor in (3), proving (4).

Now use the curve theorem for the exact \(Q_N^{\rm sh}\)
in (2). Its amplitude has a uniform positive modulus,
so the error (4), divided by its leading term, is
exponentially small, with only the factor \(N^{3/2}\).
This proves (5), uniformly through both parities and
zero charge. It does not estimate an outer cancelling
sum of those errors.

## 5. A local full-disk bridge for the shortened source

The same finite estimate gives a useful converse local
deduction. The adopted
[full-source certificate-radius theorem](research_mixed_next_full_three_certificate_packet_radius.md)
supplies a positive fixed radius \(r_{\rm full}\), with
the complete \(Q_N^{\rm full}\) packet, original holomorphic
action and nonzero amplitude, on a neighborhood of its
closed disk. No value of that radius is evaluated here.

Choose \(0<\rho<\min\{r_{\rm full},1/20\}\) so small that
\[
             \Re S(u)>M_3-\frac1{20}>\frac74
                     \qquad(|u|\le\rho).
\tag{15}
\]
This is allowed by continuity of the original action and
\(M_3>9/5\). On that disk, (3) has rate less than
\(7/6+1/20=73/60\), whose gap below \(7/4\) is \(8/15\).
After polynomial absorption, \(\Delta_N\) is therefore
exponentially smaller than the full leading packet,
uniformly on the closed disk.

Subtracting this exact difference from the full packet
gives a genuine open-disk packet for \(Q_N^{\rm sh}\),
with the same holomorphic phase and amplitude:
\[
 Q_N^{\rm sh}(u)=
 C_{N,3}N^{-3/2}A_3(0,u)e^{NS_3(0,u)}
                           \{1+O_{\rm hol}(N^{-1})\}.
\tag{16}
\]
Every fixed derivative of the normalized remainder obeys
the same bound on smaller disks, by Cauchy's formula.
This conclusion uses the uniform finite difference bound
on the whole disk, not analytic continuation from values
on a curve or from an insufficient set of physical nodes.

On the intersection with the selected curve near zero,
the two original leading amplitudes \(A_3(0,u)\) and
\(\mathcal A(u)\) agree. Indeed both normalized asymptotics
apply to the same \(Q_N^{\rm sh}\), with the same phase and
scalar; taking the limit in either parity subsequence
identifies the amplitudes. Their holomorphic germs then
agree by the identity theorem. This is a normalization
check, not an enlargement of their domains by assertion.

## Frozen source bindings

- Exact selected-curve shortened-output packet:
  e3bc75e93e1c1834faa920ff2f4ef0711c8f6cc7906b6c0c5b59bbadc86f57b7.
- Original first-edge contraction, including the odd middle row:
  b31ac2d1cbf5f0e3ab4b71b36af9718151bced51e6959ee32b26ccf7fac5dfe6.
- Original radical contraction and full Fourier coefficient bound:
  1faa5d2e02edf0a1462cc43b243e0ab4403bf56e9f1af0befb6b492441d9dd03.
- Original odd middle-row complex bound:
  c33f32be5385f98eea72a77eab211bf77229007d905b3edf598e753b4e93b057.
- Selected upper depth:
  f3b0b8f8e14adb8beff461e53ec20cdcb7afb4dc07bda3e1247116b55e13c017.
- Original selected action floor:
  492ae47bfcaa02198c0e819ef97cb9e7afb7c066d559a84373031091612b2c53.
- Full canonical certificate-radius packet:
  80fabe2d8f2cf6b129ec4c2ba27979aa70bdf0dc36da93709ca6cd6d68131a62.

